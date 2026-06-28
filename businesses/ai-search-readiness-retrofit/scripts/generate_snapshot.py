#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from datetime import datetime
import argparse, re, textwrap
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = Path('/root/ai-holding-company/businesses/ai-search-readiness-retrofit')
TEMPLATE = ROOT / 'templates/audit_template.md'
REPORTS = ROOT / 'reports/samples'

KEYWORDS = {
    'service_terms': ['service', 'repair', 'install', 'installation', 'replacement', 'maintenance', 'emergency'],
    'area_terms': ['serving', 'service area', 'near me', 'county', 'city', 'local'],
    'trust_terms': ['review', 'testimonial', 'licensed', 'insured', 'years', 'guarantee', 'certified'],
    'faq_terms': ['faq', 'frequently asked', 'questions', 'how much', 'how long', 'what is'],
    'quote_terms': ['quote', 'estimate', 'schedule', 'contact', 'call', 'book', 'request'],
}

def fetch(url: str) -> str:
    req = Request(url, headers={'User-Agent':'Mozilla/5.0 AI Search Readiness Snapshot public review'})
    with urlopen(req, timeout=12) as r:
        raw = r.read(300000)
    text = raw.decode('utf-8', errors='ignore')
    return re.sub(r'<[^>]+>', ' ', text)

def score(text: str, terms: list[str]) -> tuple[int,str]:
    low = text.lower()
    hits = [t for t in terms if t in low]
    score = min(5, len(hits))
    evidence = 'Found terms: ' + ', '.join(hits[:8]) if hits else 'No obvious public evidence found in initial page text.'
    return score, evidence

def fix(area: str, score: int) -> str:
    fixes = {
        'service':'Add clearer service list, individual service pages, and concise answer-style service summaries.',
        'area':'Add explicit city/service-area copy and local proof near quote/contact calls-to-action.',
        'trust':'Add licenses, reviews, before/after proof, warranties, team credentials, and local examples.',
        'faq':'Add FAQs that answer buyer questions in short, direct paragraphs usable by search/AI summaries.',
        'quote':'Make request-quote/contact path obvious above the fold and test it for friction.'
    }
    return fixes[area] if score < 4 else 'Maintain and expand this strength with fresh evidence and clearer structure.'

def render(args, page_text: str, fetch_error: str = ''):
    service, service_ev = score(page_text, KEYWORDS['service_terms'])
    area, area_ev = score(page_text, KEYWORDS['area_terms'])
    trust, trust_ev = score(page_text, KEYWORDS['trust_terms'])
    faq, faq_ev = score(page_text, KEYWORDS['faq_terms'])
    quote, quote_ev = score(page_text, KEYWORDS['quote_terms'])
    total = service + area + trust + faq + quote
    summary = f"Initial public-page scan scored {total}/25. " + ("Fetch issue: "+fetch_error if fetch_error else "The score is based on visible public page text only.")
    top = [
        f"1. {fix('service', service)}",
        f"2. {fix('area', area)}",
        f"3. {fix('trust', trust)}",
        f"4. {fix('faq', faq)}",
        f"5. {fix('quote', quote)}",
    ]
    vals = {
        'business_name':args.business_name, 'website':args.website, 'category':args.category, 'date':datetime.utcnow().strftime('%Y-%m-%d'),
        'executive_summary':summary,
        'service_clarity_score':service, 'service_clarity_evidence':service_ev, 'service_clarity_fix':fix('service', service),
        'service_area_score':area, 'service_area_evidence':area_ev, 'service_area_fix':fix('area', area),
        'trust_score':trust, 'trust_evidence':trust_ev, 'trust_fix':fix('trust', trust),
        'faq_score':faq, 'faq_evidence':faq_ev, 'faq_fix':fix('faq', faq),
        'quote_flow_score':quote, 'quote_flow_evidence':quote_ev, 'quote_flow_fix':fix('quote', quote),
        'top_fixes':'\n'.join(top),
        'retainer_fit':'Good fit for monthly monitoring if the business relies on local search, quote requests, reviews/proof, or service-area traffic.'
    }
    out = TEMPLATE.read_text()
    for k,v in vals.items(): out = out.replace('{{'+k+'}}', str(v))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--business-name', required=True)
    ap.add_argument('--website', required=True)
    ap.add_argument('--category', default='Local service business')
    ap.add_argument('--output')
    args=ap.parse_args()
    text=''; err=''
    try: text=fetch(args.website)
    except Exception as e: err=str(e); text=''
    report=render(args, text, err)
    safe = re.sub(r'[^a-z0-9]+','-', args.business_name.lower()).strip('-') or 'sample'
    out=Path(args.output) if args.output else REPORTS / f'{safe}-snapshot.md'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report)
    print(out)

if __name__ == '__main__': main()
