import re

def parse_number(val):
  # ignore obvious non numbers
  if(
    len(val) > 20 or
    not re.search('[0-9]', val) or
    len(val.split()) > 2 or
    ':' in val or
    re.search('[0-9][^0-9]{3,}[0-9]', val) # 24-Sept-2017
  ):
    return val

  letter_to_word = {
    'k': 'thousand',
    'm': 'million',
    'b': 'billion',
  }

  word_to_val = {
    'trillion': 10**12,
    'billion': 10**9,
    'million': 10**6,
    'thousand': 10**3,
  }

  # 6. Corporate
  lower = val.lower()
  words = lower.split()
  for word in words:
    if re.search('[a-z]{2,}', word) and word not in word_to_val:
      return val

  # "$186.7 billion" -> "186.7 billion"
  # "#36" -> "36"
  if re.match(r'^[\$#]', val):
    val = val[1:]

  # "22,349" -> "22349"
  val = re.sub(',', '', val)

  split = val.split()

  # ["6.88M"] -> ["6.88", "million"]
  if split[0][-1].isalpha():
    last_letter = split[0][-1]
    split[0] = split[0][:-1]
    split.append(letter_to_word[last_letter.lower()])

  base_val = float(split[0])

  if split[-1].isalpha():
    # ["186.7", "billion"] -> 1,867,000,000
    last_word = split[-1].lower()
    if last_word[-1] == 's':
      last_word = last_word[:-1]
    base_val *= word_to_val[last_word]
    base_val = round(base_val, 4) # floating point imprecision
  return base_val

if __name__ == '__main__':
  for in_, out in [
    ('700 untouched numbers', '700 untouched numbers'),
    ('24-Sep-2017', '24-Sep-2017'),
    ('$7.3 million', 7300000.0),
    ('22,349', 22349.0),
    ('6. Corporate', '6. Corporate'),
    ('2017-09-27T00:00:00', '2017-09-27T00:00:00'),
  ]:
    assert parse_number(in_) == out
    print('{} -> {}'.format(in_, out))

