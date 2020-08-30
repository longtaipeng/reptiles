import requests
import re
import json
import tqdm
from bs4 import BeautifulSoup
from tqdm import tqdm


# 1.采集首页信息
class Get_china_epidemic_data(object):
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_url(self, url):
        home_page = requests.get(url)
        return home_page.content.decode()

    def parse_home_page(self, home_page_data, id_number):
        soup = BeautifulSoup(home_page_data, 'lxml')
        script = soup.find(id=id_number)
        script_text = script.text
        json_data = re.findall(r'(\[.+\])', script_text)[0]
        return json.loads(json_data)

    def save(self, python_data, path):
        with open(path, 'w', encoding='utf8') as fp:
            json.dump(python_data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus_of_china(self):
        home_page_data = self.get_url(self.home_url)
        python_data = self.parse_home_page(home_page_data, 'getAreaStat')
        self.save(python_data, r'../data/china_last_all_day.json')

    # 2.获得全国信息数据
    def crawl_corona_virus(self):
        with open(r'../data/china_last_all_day.json', 'r', encoding='utf8') as fq:
            one_day_data = json.load(fq)
            # 定义一个空列表，用于存储数据
            corona_vires = []
            for city in tqdm(one_day_data, '加载中……'):
                # 3.从全国信息数据中获得各地区数据的url
                city_url = city['statisticsData']
                # 4.解析url
                city_data = self.get_url(city_url)
                city_data_python = json.loads(city_data)['data']
                # 将所有每日数据都加上省份
                for one_day in city_data_python:
                    one_day['provinceName'] = city['provinceName']
                corona_vires.extend(city_data_python)
        # 5.将所有url里面的信息都保存到文件里面
        self.save(corona_vires, '../data/china_all_city_data.json')

    def run(self):
        self.crawl_last_day_corona_virus_of_china()
        self.crawl_corona_virus()


if __name__ == '__main__':
    get_data = Get_china_epidemic_data()
    get_data.run()