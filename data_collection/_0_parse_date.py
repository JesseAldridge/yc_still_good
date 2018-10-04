import re, datetime

def month_name_to_int(month_name):
  return {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12,
  }[month_name.lower()[:3]]

def parse_date(date_str):
  if not date_str:
    return None
  lower = date_str.lower()
  # 27-sep-2017
  if re.search(r'[0-9]+-[a-z]+-[0-9]{4}', lower):
    vals = lower.split('-');
    if len(vals[0]) != 2:
      return None;
    month_int = month_name_to_int(vals[1])
    return datetime.datetime(year=int(vals[-1]), month=month_int, day=int(vals[0])).isoformat()
  # aug 31, 2018
  elif re.search(r'[a-z]+ [0-9]+, [0-9]{4}', lower):
    vals = lower.split()
    month_int = month_name_to_int(vals[0])
    return datetime.datetime(year=int(vals[-1]), month=month_int, day=int(vals[1][:-1])).isoformat()
  return lower

if __name__ == '__main__':
  print(parse_date('24-Sep-2017'))
  print(parse_date('Aug 31, 2018'))
