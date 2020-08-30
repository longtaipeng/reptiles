import json
with open(r'data/test.json', 'r', encoding='utf8') as p:
    s = p.read()
    python_str = json.loads(s)
    print(python_str)