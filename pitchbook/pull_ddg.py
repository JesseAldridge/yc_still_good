import shutil, os

import requests

if os.path.exists('ddg_results'):
  shutil.rmtree('ddg_results')
os.mkdir('ddg_results')

company_names = [
  'Airbnb',
  'Cruise',
  'DoorDash',
  'Dropbox',
  'Flexport',
  'Instacart',
  'PlanGrid',
  'Docker',
  'Segment',
  'Stripe',
  'Twitch',
  'Mixpanel',
  'Gusto',
  'Reddit',
  'Coinbase',
  'Weebly',
  'Ginkgo Bioworks',
  'Gitlab',
  'Rappi',
  'Zenefits',
]

for company_name in company_names:
  print 'company_name:', company_name
  encoded_name = company_name.replace(' ', '+')
  resp = requests.get('https://duckduckgo.com/html/?q={}+pitchbook'.format(encoded_name))
  path = os.path.join('ddg_results', '{}.html').format(company_name)
  with open(path, 'w') as f:
    f.write(resp.content)
