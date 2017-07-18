#python3标准数据类型有6种
#Number（数字）
#String（字符串）
#List（列表）
#Tuple（元组）
#Set（集合）
#Dictionary（字典）


#Number
#内置的type()函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
#也可以用isinstaance()来判断
x = 123
print(isinstance(a, int))
#isinstance和type的区别
#type()不会认为子类是一种父类类型
#isinstance()会认为子类是一种父类类型
print(10 * '*', 'isinstance和type的区别' , 10 * '*')
class A:
	pass
class B(A):
	pass
print(isinstance(A(), A))  # returns True
print(type(A()) == A)      # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)      # returns False


#String
#python中的字符有两种索引方式，从左往右以0开始，从右往左以-1开始
#python中的字符串不能改变
print(10 * '*', '字符串的截取' , 10 * '*')
str = 'Hello World, Hi Python!'
print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符
print(str[0])       # 输出字符串第一个字符
print(str[2:8])     # 输出从第三个开始到第八个的字符
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次
print(str + "TEST") # 连接字符串


#List
#python中list的索引值以0为开始值，-1为从末尾的开始位置。
#list中的元素是可变的
print(10 * '*', 'List' , 10 * '*')
list = ['abcd', 786 , 9.13, 'Hello', 73.8]
tinyList = [123, 'World']
print(list)            # 输出完整列表
print(list[0])         # 输出列表第一个元素
print(list[1:3])       # 从第二个开始输出到第三个元素
print(list[2:])        # 输出从第三个元素开始的所有元素
print(tinyList * 2)    # 输出两次列表
print(list + tinyList) # 连接列表


#Tuple
#元组与列表类似，但元组的元素不能被修改
print(10 * '*', 'Tuple' , 10 * '*')
tuple = ['abcd', 786 , 9.13, 'Hello', 73.8]
tinyTuple = [123, 'World']
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinyTuple * 2)     # 输出两次元组
print (tuple + tinyTuple) # 连接元组


#Set
#集合是一个无序不重复元素的序列
#基本功能是进行成员关系测试和删除重复元素
print(10 * '*', 'Set' , 10 * '*')
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉 
# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)     # a和b的差集 
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素


#Dictionary
#字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
#键(key)必须使用不可变类型。
#在同一个字典中，键(key)必须是唯一的。
print(10 * '*', 'Dictionary' , 10 * '*')
dict = {}
dict['one'] = "1 - Hello"
dict[2] = "2 - World"
tinyDict = {'name': 'SunnyChen','code':1, 'site': 'www.github.com/chenqim'}
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (dict)
print (tinyDict)          # 输出完整的字典
print (tinyDict.keys())   # 输出所有键
print (tinyDict.values()) # 输出所有值
#构造函数dict()可以直接从键值对序列中构建字典如下
#想要调用构造方法则必须将之前定义过的dict删除，不然报"TypeError: 'dict' object is not callable"的错误
del(dict)
print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
print({x: x**2 for x in (2, 4, 6)})
print(dict(Runoob=1, Google=2, Taobao=3))





