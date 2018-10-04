import re

import _0_utils, _0_parse_date, _0_parse_number

def cleanup_collection(collection):
  if isinstance(collection, dict):
    key_vals = collection.items()
  else:
    key_vals = enumerate(collection)

  for key, val in key_vals:
    if isinstance(val, dict) or isinstance(val, list):
      cleanup_collection(val)
    elif isinstance(val, str):
      val = _0_parse_date.parse_date(val)
      collection[key] = _0_parse_number.parse_number(val)

merged = _0_utils.load_json('_2_merged.json')
cleanup_collection(merged)
_0_utils.write_json('_3_numbers.json', merged)
