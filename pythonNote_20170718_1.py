#python基础知识


#保留字，即关键字
#输出所有的关键字
import keyword
print(keyword.kwlist)

	
#这是一个单行注释
print('Hello, World!') #这也是一个单行注释
'''
这是一个多行注释的第一行
这是一个多行注释的第二行
这是一个多行注释的第三行
。。。
'''	


#if条件判断
#用缩进来表示代码块，不需要使用{}，但在条件完时需要加:
#缩进的空格数是可变的，但相同的代码块需要有相同的缩进
if 1 == 1:
	print('Hello, World!')
else:
	print('Oh, No!')


#多行语句
total = '这是一条很长的语句，' + '这是第一行，' + \
		'这是第二行，' + \
		'这是第三行。'
print(total)
	

#python中数据类型分四种：整数、长证书、浮点数和复数
#整数， 如 1
#长整数 是比较大的整数
#浮点数 如 1.23、3E-2
#复数 如 1 + 2j、 1.1 + 2.2j


#字符串
#python中单引号和双引号完全相同
#使用三引号（'''或"""）可以指定一个多行字符串
#转义符 '\'
#自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
#python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
#字符串是不可变的。
#按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成,
按照原样输出。"""
print(paragraph)


#等待用户输入
#简易实现两个数的加法
num1 = input('请输入第一个数：')
num2 = input('请输入第二个数：')
print(float(num1) + float(num2))


#同一行显示多条语句
#若要在同一行使用多条语句，要使用分号分隔开
str1 = 'Hello';str2 = ', World!';print(str1 + str2)


#print输出
#print默认输出是换行的，如果要实现不换行需要在变量末尾加上end=""
x="a"
y="b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end="")


#import与from...import
#在python用import或者from...import来导入相应的模块。
#将整个模块(somemodule)导入，格式为：import somemodule
#从某个模块中导入某个函数,格式为：from somemodule import somefunction
#从某个模块中导入多个函数,格式为：from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为：from somemodule import *










