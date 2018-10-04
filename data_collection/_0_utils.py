import json, codecs

def load_json(path):
  with codecs.open(path, encoding='utf8') as f:
    text = f.read()
  return json.loads(text)

def write_json(path, data_obj):
  json_str = json.dumps(data_obj, indent=2, ensure_ascii=False, separators=(',', ': '))
  with codecs.open(path, encoding='utf8', mode='w') as f:
    f.write(json_str)

if __name__ == '__main__':
  def test():
    test_filename = '_0_countries_manual.json'
    dict1 = load_json(test_filename)
    write_json(test_filename, dict1)
    dict2 = load_json(test_filename)
    print('dict1:', dict1)
    print('dict2:', dict2)
    assert dict1 == dict2
  test()
