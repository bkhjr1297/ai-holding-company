#!/usr/bin/env python3
from __future__ import annotations
import csv, re, ssl, time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

BASE = Path('/root/ai-holding-company/businesses/ai-search-readiness-retrofit')
CRM = BASE / 'crm/pipeline.csv'
OUT = BASE / 'outreach/contact_research.csv'
EMAIL_RE = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}')
BAD_EMAIL_BITS = ['example.com', 'domain.com', 'email.com', 'yourdomain', 'sentry', 'wixpress', 'schema.org']
CTX = ssl.create_default_context()


def fetch(url: str, timeout=12) -> str:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 Revenue Rescue Desk public contact research'})
    with urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read(500000).decode('utf-8', errors='ignore')


def clean_emails(text: str):
    emails = sorted(set(e.strip('.,;:()[]<>').lower() for e in EMAIL_RE.findall(text)))
    return [e for e in emails if not any(bad in e for bad in BAD_EMAIL_BITS)]


def contact_links(base_url: str, html: str):
    links = []
    for href, label in re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.I | re.S):
        raw = re.sub(r'<[^>]+>', ' ', label).strip().lower()
        hlow = href.lower()
        if 'mailto:' in hlow:
            links.append(href)
        elif any(k in hlow or k in raw for k in ['contact', 'quote', 'estimate', 'schedule', 'request-service', 'service-request']):
            links.append(urljoin(base_url, href))
    # common guesses
    for suffix in ['/contact', '/contact-us', '/request-service', '/schedule-service', '/get-a-quote', '/free-estimate']:
        links.append(urljoin(base_url, suffix))
    seen=[]
    for l in links:
        if l not in seen:
            seen.append(l)
    return seen[:8]


def main():
    rows = list(csv.DictReader(CRM.open()))
    out = []
    for r in rows:
        if r.get('category') == 'HVAC':
            continue
        url = r.get('website','')
        if not url:
            continue
        emails=[]; links=[]; status='ok'
        try:
            html = fetch(url)
            emails += clean_emails(html)
            links = contact_links(url, html)
            # fetch likely contact pages for more emails
            for link in links[:4]:
                if link.startswith('mailto:'):
                    emails.append(link.split(':',1)[1].split('?')[0].lower())
                    continue
                try:
                    chtml = fetch(link, timeout=8)
                    emails += clean_emails(chtml)
                    time.sleep(0.3)
                except Exception:
                    pass
        except Exception as e:
            status = f'fetch_error: {e}'[:120]
        emails = sorted(set(e for e in emails if e))
        out.append({
            'company': r.get('company',''),
            'website': url,
            'category': r.get('category',''),
            'score': r.get('score',''),
            'emails': ';'.join(emails[:5]),
            'primary_email': emails[0] if emails else '',
            'contact_pages': ';'.join([l for l in links if not l.startswith('mailto:')][:5]),
            'status': status if (emails or links) else 'no_public_contact_found'
        })
        time.sleep(0.5)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['company','website','category','score','emails','primary_email','contact_pages','status'])
        w.writeheader(); w.writerows(out)
    print(OUT)
    print('rows', len(out), 'with_email', sum(1 for x in out if x['primary_email']), 'with_contact_page', sum(1 for x in out if x['contact_pages']))

if __name__ == '__main__':
    main()
