import json
# 获取到python数据
json_str = """[{"id":5183280,"createTime":1598597044000,"modifyTime":1598597044000,
"tags":"","countryType":2,"continents":"北美洲"}]"""
rs = json.loads(json_str)

# 转化成json数据
json_str = json.dumps(rs, ensure_ascii=False)

with open(r'../data/test1.json', 'w', encoding='utf8') as a:
    json.dump(rs, a)