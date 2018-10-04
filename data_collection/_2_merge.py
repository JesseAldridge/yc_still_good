import json, re

import slugify

import _0_utils

def merge_with_main(new_dict, name_to_full_dict):
  for name_key in new_dict:
    if 'name' in name_key:
      break
  slug = slugify.slugify(new_dict[name_key])
  del new_dict[name_key]
  alias_to_norm_name = {
    'usa': 'united states',
  }
  slug = alias_to_norm_name.get(slug, slug)
  new_dict['slug'] = slug
  name_to_full_dict.setdefault(slug, {'slug': slug})
  for key, attr in new_dict.items():
    name_to_full_dict[slug][key] = attr

def merge_all_with_main(partial_dicts, name_to_full_dict):
  for partial_dict in partial_dicts:
    merge_with_main(partial_dict, name_to_full_dict)

def main():
  name_to_full_dict = {}

  company_deals = _0_utils.load_json('partial_json/deals.json')
  merge_all_with_main(company_deals, name_to_full_dict)

  funding = _0_utils.load_json('partial_json/funding.json')
  merge_all_with_main(funding, name_to_full_dict)

  valuations = _0_utils.load_json('partial_json/valuations.json')
  merge_all_with_main(valuations, name_to_full_dict)

  # Sanity check
  for company_dict in name_to_full_dict.values():
    assert len(company_dict) > 1

  # Output
  _0_utils.write_json('_2_merged.json', name_to_full_dict)

if __name__ == '__main__':
  main()
