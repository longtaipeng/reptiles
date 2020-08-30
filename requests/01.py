import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get('https://python123.io/ws/demo.html')

# requests.encoding = 'utf8'

# text = response.content.decode()
soup = BeautifulSoup(response.text,'lxml')

# 查找第一个<a>标签
# a = soup.find('a')

# 查找所有的<a>标签，返回列表
# a = soup.find_all('a')

# 通过命名参数来指定查找
# a = soup.find(class='py1')

# 通过attrs来指定属性字典进行查找
a = soup.find(attrs={'class':'py1'})

# 通过文本内容进行查找
# a = soup.find(text='Basic Python')

# Tag对象 
# print(type(a)) #<class 'bs4.element.Tag'>

# 获取标签名字
print('获取标签名字: ', a.name)

# 获取标签所有属性
print('获取标签所有属性: ', a.attrs)

# 获取标签文本内容
print('获取标签文本内容: ', a.text)