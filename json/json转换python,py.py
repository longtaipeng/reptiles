# json字符串转换为python数据

# 导入模块
import json

# 1.准备json字符串
json_str = """[{"id":5183280,"createTime":1598597044000,"modifyTime":1598597044000,
"tags":"","countryType":2,"continents":"北美洲"}]"""

# 2.把json字符串转化为python数据 --> loads 方法就是将转换方法
rs = json.loads(json_str)


# json文件转化为python数据 --> load 方法就是转化方法
with open(r'../data/test.json','r', encoding='utf8') as a:
    python_list = json.load(a)

print(rs)


