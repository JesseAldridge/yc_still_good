import re, urllib, glob, json, os

company_dicts = []
for path in glob.glob('ddg_results/*.html'):
  with open(path) as f:
    text = f.read()

  for h2_match in re.finditer('<h2 class="result__title">.+?</h2>', text, re.DOTALL):
    if len(h2_match.group(0)) > 1000: # skip ads
      continue
    h2_text = h2_match.group(0)
    if 'profiles' not in h2_text or 'company' not in h2_text:
      continue
    match = re.search('uddg=(.+?)"', h2_text)
    url_encoded = match.group(1)
    url_decoded = urllib.unquote(url_encoded).decode('utf8')

    company_dict = {
      "name": os.path.basename(path).rsplit('.html')[0],
      "pitchbook_url": url_decoded,
    }

    company_dicts.append(company_dict)
    print 'url:', url_decoded
    break


json_out = json.dumps(company_dicts, indent=2)
with open('companies.json', 'w') as f:
  f.write(json_out)

