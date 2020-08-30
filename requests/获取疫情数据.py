# 导入模块
import requests
from bs4 import BeautifulSoup

# 发送请求,获取数据
data = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
home_text = data.content.decode()

# 创建soup对象
soup = BeautifulSoup(home_text, 'lxml')
# 在soup对象里面查找指定对象内容
script = soup.find(id='getListByCountryTypeService2true')
text = script.text
print(text)