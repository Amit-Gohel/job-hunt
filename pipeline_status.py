import json, glob
results = []
for path in glob.glob('company/*/tracker.json'):
    with open(path) as f:
        t = json.load(f)
    slug = t.get('slug','')
    rs = t.get('research_status','not_started')
    contacts = t.get('contacts', [])
    emails_sent = sum(1 for c in contacts if c.get('date_sent',''))
    all_drafted = all(c.get('content','').strip() for c in contacts) if contacts else False
    has_tailoring = bool(t.get('tailoring_notes','').strip())
    pipeline_complete = rs=='done' and has_tailoring and all_drafted and len(contacts)>0
    status = 'COMPLETE' if pipeline_complete else ('IN_PROGRESS' if rs=='done' else 'NOT_STARTED')
    priority = t.get('metadata',{}).get('priority_score',0)
    source = t.get('metadata',{}).get('_source_csv','')
    results.append((priority, slug, status, len(contacts), emails_sent, all_drafted, source))
results.sort(key=lambda x: -x[0])
print("=== company_data_1.csv ===")
for r in results:
    if 'company_data_1' in r[6]:
        print(r[0], r[1], r[2], 'c='+str(r[3]), 'sent='+str(r[4]))
print()
print("=== company_data_2.csv ===")
for r in results:
    if 'company_data_2' in r[6]:
        print(r[0], r[1], r[2], 'c='+str(r[3]), 'sent='+str(r[4]))
