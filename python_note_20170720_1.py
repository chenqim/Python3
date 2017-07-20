#if语句
#if语句实例
#该实例模拟计算了狗狗的年龄
age = int(input("请输入你家狗狗的年龄："))
print('')
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)
### 退出提示
input("点击 enter 键退出")


#while语句
#while语句实例
#该实例演示了数字猜谜游戏
print(10 * '*', 'while语句', 10 * '*')
import random
print("数字猜谜游戏!")
#用于生成[0,99]区间的随机数
number = random.randint(0, 99)
print("答案：", number)
guess = -1
while guess != number: 
    try:
        guess = int(input("请输入你猜的数字："))
        if guess == number:
            print("恭喜，你猜对了！")
        elif guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")
    except ValueError:
	    print("输入不合法，请输入有效数字")
### 退出提示
input("点击 enter 键退出")


#while...else语句
#当条件语句为false的时候会执行else语句块
print(10 * '*', 'while...else语句', 10 * '*')
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "等于5")


#for循环
#for循环语句实例
print(10 * '*', 'for语句', 10 * '*')
languages = ["C", "Java","Python","C++"]
for language in languages:
    if language == "Python":
        print("Python is cool!")
        break
    print("循环数据 " + language)
else:
    print("没有循环数据!")
print("完成循环!")


#range()函数
print(10 * '*', 'range函数', 10 * '*')
#输出[0,5]
for i in range(5):
    print(i)
#输出[5,9]
for j in range(5, 9):
    print(j)
#输出0,3,6,9
for k in range(0, 10, 3):
    print(k)

	
#函数
#函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
#任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
#函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
#函数内容以冒号起始，并且缩进。
#return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None。
#函数实例
#计算面积函数
print(10 * '*', '函数', 10 * '*')
def area(width, height):
    return width * height 
def print_welcome(name):
    print("Welcome", name)
print_welcome("SunnyChen")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


#函数传不可变对象
'''
实例中有 int 对象 2，
指向它的变量是 b，
在传递给 ChangeInt 函数时，
按传值的方式复制了变量 b，
a 和 b 都指向了同一个 Int 对象，
在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。
'''
def ChangeInt( a ):
    a = 10
b = 2
ChangeInt(b)
print(b) #结果是 2
#函数传可变对象
#传入函数的和在末尾添加新内容的对象用的是同一个引用
#可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]);
   print ("函数内取值: ", mylist)
   return
mylist = [10,20,30];
changeme( mylist );
print ("函数外取值: ", mylist) #函数内外取值相同
'''
总结：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
'''


#全局变量和局部变量
'''
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。
'''
print(10 * '*', '作用域', 10 * '*')
total = 0 #这是一个全局变量
#可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 #total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)


'''
global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
'''
#以下实例修改全局变量num
num = 1
def fun1():
    global num  #需要使用 global 关键字声明
    print(num)  #输出1
    num = 123
    print(num)  #输出123
fun1()


#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)     #输出100
    inner()
    print(num)         #输出100
outer()