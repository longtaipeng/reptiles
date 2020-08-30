import requests
from bs4 import BeautifulSoup
import json
import re
# 获取疫情首页
s = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
s_text = s.content.decode()

# 提取数据
soup = BeautifulSoup(s_text, 'lxml')
data = soup.find(attrs={'id': "getListByCountryTypeService2true"})
text = data.text

# 从数据中获取json字符串
json_str = re.findall(r'(\[.+\])', text)[0]

# 将json字符串转化为python类型数据
python_str = json.loads(json_str)

# 以json格式保存数据
with open(r'../data/test.json', 'w', encoding='utf8') as a:
    json.dump(python_str, a)
