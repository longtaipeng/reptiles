import requests
from bs4 import BeautifulSoup
import json
import re
# 进度条
from tqdm import tqdm


class Epidemic_data(object):

    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self, url):
        """
        根据URL，获取网页内容
        :param url: 请求的URl
        :return: 网页内容字符串
        """
        response = requests.get(url)
        return response.content.decode()

    def parse_home_page(self, home_page, id_number):
        """
        解析网页内容，获取解析后的python数据
        :param id_number: 数据借口
        :param home_page:网页内容
        :return:解析后的python数据
        """
        # 提取数据
        soup = BeautifulSoup(home_page, 'lxml')
        data = soup.find(id=id_number)
        text = data.text

        # 从数据中获取json字符串
        json_str = re.findall(r'(\[.+\])', text)[0]

        # 将json字符串转化为python类型数据
        data = json.loads(json_str)
        return data

    def save(self, data, path):
        """
        保存采集到的内容
        :param data:数据
        :param path:保存目录
        :return:
        """
        # 以json格式保存数据
        with open(path, 'w', encoding='utf8') as a:
            json.dump(data, a, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """

        :return:
        """
        # 1.发送请求，获取首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2.解析内容
        last_day_data = self.parse_home_page(home_page, 'getListByCountryTypeService2true')
        # 3.保存数据
        self.save(last_day_data, r'../data/test.json')

    def crawl_corona_virus(self, start_path, description, end_path):
        """
        采集数据模板
        :return:
        """
        # 1.获取疫情数据
        with open(start_path, encoding='utf8') as fp:
            last_data = json.load(fp)
            # 定义一个列表用于保存数据
            corona_vires = []
            for country in tqdm(last_data, description):
                # 2.获取到疫情统计数据的URL
                statistics_data_url = country['statisticsData']
                # 3.发送请求，获取json数据
                statistics_data_url_json_str = self.get_content_from_url(statistics_data_url)
                # 4.将json数据转化为python数据
                statistics_data_url_python_data = json.loads(statistics_data_url_json_str)['data']
                for one_day in statistics_data_url_python_data:
                    one_day['provinceName'] = country['provinceName']
                    if country.get('countryShortCode'):
                        one_day['countryShortCode'] = country['countryShortCode']
                corona_vires.extend(statistics_data_url_python_data)
            # 5.保存数据
        self.save(corona_vires, end_path)

    def crawl_last_day_corona_virus_of_china(self):
        """
        采集最近一日国内各省疫情数据
        1. 采集首页数据
        2. 解析首页数据，获取最近一日国内疫情数据
        3.保存疫情数据
        :return:
        """
        # 1. 采集首页数据
        home_page = self.get_content_from_url(self.home_url)
        # 将json字符串转化为python数据
        last_day_data_python = self.parse_home_page(home_page, 'getAreaStat')
        # 保存
        self.save(last_day_data_python, r'../data/china_last_day.json')

    def code_data(self):
        self.crawl_corona_virus('../data/test.json', '获取全球疫情数据中 ', '../data/one_day_data.json')
        self.crawl_corona_virus('../data/china_last_day.json', '获取全国疫情数据中 ', '../data/china_all_city_data.json')

    def run(self):
        self.crawl_last_day_corona_virus()
        self.crawl_last_day_corona_virus_of_china()
        self.code_data()


if __name__ == '__main__':
    spider = Epidemic_data()
    spider.run()