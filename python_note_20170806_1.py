'''
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。
Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
json.dumps(): 对数据进行编码。
json.loads(): 对数据进行解码。
'''


import json
# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Baidu',
    'url' : 'http://www.baidu.com'
}
json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])
# Python list类型转换为 JSON 对象
data3 = ['Hello', 'World', 123, 'sunny', 'chen', '888']
json_str2 = json.dumps(data3)
print ("Python 原始数据：", repr(data3))
print ("JSON 对象：", json_str2)


# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
# 写入 JSON 数据
data = {"no": 1, "name": "Baidu", "url": "http://www.baidu.com"}
with open('tmp/data.json', 'w') as f:
    json.dump(data, f)
# 读取数据
with open('tmp/data.json', 'r') as f:
    datas = json.load(f)
    print(datas)