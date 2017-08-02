'''
爬取简单的城市加温度数据
'''

# coding : UTF-8

import urllib.request
import re
import codecs
from bs4 import BeautifulSoup

#定义一个写入文本的函数
def writetxt(path, content, code):
    with codecs.open(path, 'a', encoding=code) as f:
        f.write(content)
    return path + ' is ok!'

def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    page.close()
    return html

def get_weather(html):
    final = []
    bs = BeautifulSoup(html, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body # 获取body部分
    ul = body.find('ul', {'class': 'clearfix city'})  # 找到class为clearfix city的ul
    # ul = data.find('ul')  # 获取ul部分
    # li = ul.find_all('li')  # 获取所有的li
    # weatherList = re.compile(reg).findall(html)
    li = ul.find_all('li')
    for day in li:
        temp = []
        city = day.find('span').string
        tempurature = day.find('i').string
        temp.append(city)
        temp.append(tempurature)
        final.append(temp)
    return final

if __name__ == '__main__':
    # url = 'http://nb.zj.weather.com.cn/'
    url = 'http://www.weather.com.cn/weather1d/101210401.shtml#input'
    html = get_html(url)
    # print(html)
    weather = str(get_weather(html))
    print(writetxt('weather.txt', weather, 'utf-8'))
    print(weather)