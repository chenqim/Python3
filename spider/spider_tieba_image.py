import urllib
import urllib.request
import re

def get_html(url):
    # 添加headers，伪装成浏览器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    # 构建请求
    request = urllib.request.Request(url, headers = headers)
    # 获取服务器响应
    response = urllib.request.urlopen(request)
    # 读取页面
    html = response.read()
    return html

def get_image(html):
    # 利用正则表达式匹配网页内容找到图片地址
    reg = r'src="(https://img.*?\.jpg)" size'
    pattern = re.compile(reg)
    # repr用来转换表达式类型字符串
    image_url_list = re.findall(pattern, repr(html))
    # print(image_url_list)
    num = 1
    for image_url in image_url_list:
        '''
        重复爬取会导致原先下载好的图片被覆盖，所以最好分文件夹
        下载图片也可以用：urllib.request.urlretrieve(img_url,'C:/users/xm/desktop/python/spider/img/%s.jpg' %num)
        这一部分最好加上异常处理
        '''
        # 循环获取到的图片路径，并将每个路径重新解析
        image = get_html(image_url)
        print('正在下载第%s张图片'%num)
        print(image_url)
        # 下载图片到本地
        with open('C:/users/xm/desktop/python/spider/img/%s.jpg' %num, 'wb') as fp:
            fp.write(image)
            num += 1
    return

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/5252908812'
    html = get_html(url)
    get_image(html)
    print('Download complete!')