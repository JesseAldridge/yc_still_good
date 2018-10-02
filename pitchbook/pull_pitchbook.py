import json, shutil, os

import requests

with open('companies.json') as f:
  companies_json = f.read()
company_dicts = json.loads(companies_json)

if os.path.exists('pitchbook_results'):
  shutil.rmtree('pitchbook_results')
os.mkdir('pitchbook_results')

for company_dict in company_dicts:
  print 'pulling:', company_dict['name']
  resp = requests.get(company_dict['pitchbook_url'])
  path = os.path.join('pitchbook_results', company_dict['name']) + '.html'
  with open(path, 'w') as f:
    f.write(resp.content)
