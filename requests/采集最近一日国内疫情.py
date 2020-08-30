import requests
from bs4 import BeautifulSoup
import re
import tqdm
import json

# 1.获取首页数据
home_page = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page_text = home_page.content.decode()

# 2.提取对应数据
soup = BeautifulSoup(home_page_text, 'lxml')
script = soup.find(id='getAreaStat')
script_text = script.text
china_last_day_data = re.findall(r'(\[.+\])', script_text)[0]


# 3.将json数据转化为python数据
china_last_day_data_python = json.loads(china_last_day_data)

# 4.将python数据保存在文件内
with open(r'../data/china_last_day.json', 'w', encoding='UTF8') as fp:
    json.dump(china_last_day_data_python, fp, ensure_ascii=False)

