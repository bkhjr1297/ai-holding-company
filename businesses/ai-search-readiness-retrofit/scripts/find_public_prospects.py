#!/usr/bin/env python3
"""Find public prospect websites using OpenStreetMap Overpass where possible.
No emails are sent. No forms are submitted.
"""
from __future__ import annotations
import argparse, csv, json, time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

OUT = Path('/root/ai-holding-company/businesses/ai-search-readiness-retrofit/data/prospects.csv')
OVERPASS = 'https://overpass-api.de/api/interpreter'
QUERIES = {
  'HVAC': ['hvac', 'heating', 'air conditioning'],
  'Plumbing': ['plumber', 'plumbing'],
  'Roofing': ['roofer', 'roofing']
}

def overpass_query(city: str, terms: list[str], limit: int) -> str:
    # Search named amenities/shops/offices with website tags near a city area.
    regex = '|'.join(terms)
    return f"""
[out:json][timeout:25];
area["name"="{city}"]["boundary"="administrative"]->.searchArea;
(
  nwr(area.searchArea)["website"]["name"~"."]["name"~"{regex}",i];
  nwr(area.searchArea)["contact:website"]["name"~"."]["name"~"{regex}",i];
);
out tags {limit};
"""

def fetch(city, category, limit):
    q = overpass_query(city, QUERIES[category], limit)
    data = urlencode({'data': q}).encode()
    req = Request(OVERPASS, data=data, headers={'User-Agent':'Revenue Rescue Desk public prospect research'})
    with urlopen(req, timeout=35) as r:
        return json.loads(r.read().decode())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--city', default='Tampa')
    ap.add_argument('--limit', type=int, default=25)
    args=ap.parse_args()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows=[]
    for cat in QUERIES:
        try:
            data=fetch(args.city, cat, args.limit)
            for el in data.get('elements',[]):
                tags=el.get('tags',{})
                website=tags.get('website') or tags.get('contact:website') or ''
                name=tags.get('name') or ''
                if name and website:
                    rows.append({'company':name,'website':website,'category':cat,'source':'openstreetmap_overpass','status':'new'})
        except Exception as e:
            rows.append({'company':f'RESEARCH_BLOCKED_{cat}','website':'','category':cat,'source':'overpass_error','status':str(e)[:120]})
        time.sleep(1)
    # fallback seed if API returns nothing
    if not any(r.get('website') for r in rows):
        rows.extend([
          {'company':'Example HVAC Company','website':'https://example.com','category':'HVAC','source':'fallback_seed','status':'needs_real_public_target'},
          {'company':'Example Plumbing Company','website':'https://example.org','category':'Plumbing','source':'fallback_seed','status':'needs_real_public_target'},
          {'company':'Example Roofing Company','website':'https://example.net','category':'Roofing','source':'fallback_seed','status':'needs_real_public_target'},
        ])
    seen=set(); dedup=[]
    for r in rows:
        key=(r['company'].lower(), r['website'].lower())
        if key in seen: continue
        seen.add(key); dedup.append(r)
    with OUT.open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=['company','website','category','source','status'])
        w.writeheader(); w.writerows(dedup)
    print(OUT)
    print('rows', len(dedup), 'with_websites', sum(1 for r in dedup if r['website']))

if __name__=='__main__': main()
