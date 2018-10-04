import json, re, glob, os

import _0_parser as parser, _0_utils as utils

def parse_company(path):
  SEEK_FUNDING, SEEK_DATE = 0, 1

  with open(path) as f:
    text = f.read()
  parser_ = parser.Parser(text)
  funding_count = 3
  state = SEEK_FUNDING
  for _ in range(10 ** 6):
    print(parser_.status_str())
    if parser_.is_done():
      break

    line = parser_.next_line()
    if state == SEEK_FUNDING:
      if re.search('^Funding Rounds$', line):
        funding_count -= 1
        if funding_count == 0:
          state = SEEK_DATE
    elif state == SEEK_DATE:
      if re.search('^[A-Z][a-z]{2} [0-9]+, [0-9]{4}$', line):
        round_dicts = []

        for _ in range(10 ** 6):
          date_str = parser_.line()
          parser_.next_line()
          parser_.next_line()
          split = parser_.next_line().split()
          num_investors, amount, who = split[0], split[1], ' '.join(split[2:])
          round_dicts.append({
            "date_str": date_str,
            "amount": amount,
            "num_investors": num_investors,
            "who": who,
          })
          next_line = parser_.next_line()
          if not re.search('^[A-Z][a-z]{2} [0-9]+, [0-9]{4}$', next_line):
            return round_dicts

def txt_dump_to_dicts():
  companies = []
  for path in glob.glob('crunchbase_dumps/*.txt'):
    name = os.path.basename(path).rsplit('.txt', 1)[0]
    round_dicts = parse_company(path)
    companies.append({"name": name, "rounds": round_dicts})
  return companies

def main():
  companies = txt_dump_to_dicts()
  path = os.path.expanduser('~/Dropbox/yc_still_good/data_collection/partial_json/funding.json')
  utils.write_json(path, companies)

if __name__ == '__main__':
  main()
