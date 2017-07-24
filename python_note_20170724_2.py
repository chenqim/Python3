# python的输出
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
hello = 'Hello, World!\n'
hello1 = str(hello)
print('hello1:', hello1)
# repr()函数可以转义字符串中的特殊字符
hello2 = repr(hello)
print('hello2:', hello2)
# repr()的参数可以是 Python 的任何对象
x = 10 * 3.25
y = 200 * 200
print(repr((x, y, ('Google', 'Runoob'))))


# 这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
print(10 * '*', 'rjust方法' , 10 * '*')
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))


# zfill()方法会在数字左边填充0
print(10 * '*', 'zfill方法' , 10 * '*')
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))


# str.format()基本使用方法
print(10 * '*', 'str.format()' , 10 * '*')
print('{}网址： "{}"'.format('百度', 'www.baidu.com'))
print('{0} 和 {1}'.format('Google', 'Baidu'))
print('{1} 和 {0}'.format('Google', 'Baidu'))
print('{name}网址： {site}'.format(name='百度', site='www.baidu.com'))
print('站点列表： {0}, {1}, 和 {other}。'.format('Google', 'Baidu', other='Taobao'))


import math
print('常量 PI 的值近似为： {}。'.format(math.pi))
# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位
print('常量 PI 的值近似为： {0:.3f}。'.format(math.pi))
# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))
# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值
table = {'Google': 1, 'Baidu': 2, 'Taobao': 3}
print('Runoob: {0[Baidu]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))


# python的标准输入
str = input("请输入：");
print ("你输入的内容是: ", str)


# python文件的读写
# 打开一个文件
# 第一个参数为要打开的文件名
# 第二个参数描述文件如何使用的字符，参数是可选的，'r' 将是默认值
# 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写
# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
print(10 * '*', 'f.write()' , 10 * '*')
f = open("tmp/python.txt", "w")
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()
print('file is ok')

# 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回
# size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回
print(10 * '*', 'f.read()' , 10 * '*')
f = open("tmp/python.txt", "r")
s = f.read()
print(s)
# 关闭打开的文件
f.close()
# f.readline()：会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# f.readlines()：将返回该文件中包含的所有行，如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。


# 如果要写入一个不是字符串的东西，则需要先转换
f = open("tmp/tuple.txt", "w")
value = ('www.baidu.com', 14)
del(str)
s = str(value)
f.write(s)
# 关闭打开的文件
f.close()