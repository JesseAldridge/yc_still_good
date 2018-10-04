import re, urllib, glob, json, os

company_dicts = []
for path in glob.glob('pitchbook_results/*.html'):
  company_name = os.path.basename(path).rsplit('.html', 1)[0]

  with open(path) as f:
    text = f.read()

  match = re.search('<div class="data-table">.+?</div>', text, re.DOTALL)
  table_text = match.group(0)
  match = re.search('<h2>(.+?)</h2>', table_text, re.DOTALL)
  table_name = match.group(1)
  print 'table_text:', table_text

  match = re.search('<thead>.+?</thead>', text, re.DOTALL)
  table_head = match.group(0)
  column_names = []
  for match in re.finditer('<th class=".+?">(.+?)</th>', table_head):
    column_names.append(match.group(1))

  match = re.search('<tbody>.+?</tbody>', text, re.DOTALL)
  table_body = match.group(0)
  deals = []
  for match_row in re.finditer('<tr>(.+?)</tr>', table_body, re.DOTALL):
    row = match_row.group(0)
    vals = []
    for match_col in re.finditer('<td class=".+?">(.+?)</td>', row):
      vals.append(match_col.group(1))
    row_dict = {}
    for name, val in zip(column_names, vals):
      row_dict[name] = val
    deals.append(row_dict)
  company_dicts.append({
    "company_name": company_name,
    "deals": deals,
  })

json_out = json.dumps(company_dicts, indent=2)
with open('deals.json', 'w') as f:
  f.write(json_out)
