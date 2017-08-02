'''''
第一个示例：简单的网页爬虫
爬取豆瓣首页
同级目录下有有无douban.html文本文件都可以
'''

import urllib.request
import codecs

#定义一个写入文本的函数
def writetxt(path, content, code):
    with codecs.open(path, 'a', encoding=code) as f:
        f.write(content)
    return path + ' is ok!'

#网址
url = "http://www.douban.com/"

#请求
request = urllib.request.Request(url)

#爬取结果
response = urllib.request.urlopen(request)

data = response.read()

#设置解码方式
data = data.decode('utf-8')

#在控制台打印结果
#print(data)

#将爬到的内容写入文本文件中
result = writetxt('douban.html', data, 'utf-8')
print(result)

#打印爬取网页的各类信息
#print(type(response))
#print(response.geturl())
#print(response.info())
#print(response.getcode())