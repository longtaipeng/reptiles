# 导入模块
import requests
from bs4 import BeautifulSoup
import re
import json
# 发送请求,获取数据
data = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
home_text = data.content.decode()

# 创建soup对象
soup = BeautifulSoup(home_text, 'lxml')
# 在soup对象里面查找指定对象内容
script = soup.find(id='getListByCountryTypeService2true')
text = script.string
# 使用正则提取json字符串
json_str = re.findall(r'\[.+\]', text)[0]
# 将json字符串转化为python数据
python_str = json.loads(json_str)
print(python_str)