'''
list常用方法：
list.append(x)	    把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	    通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，
                    例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	    删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	    从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。
                    （方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	    移除列表中的所有项，等于del a[:]。
list.index(x)	    返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	    返回 x 在列表中出现的次数。
list.sort()	        对列表中的元素进行排序。
list.reverse()	    倒排列表中的元素。
list.copy()	        返回列表的浅复制，等于a[:]。
'''


# 将列表当作堆栈使用
# 堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）
# 先append()再pop()就可以模拟这一现象
print(10 * '*', '列表', 10 * '*')
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print('释放前：',stack)
stack.pop()
print('释放后：', stack)
stack.pop()
print('再释放：', stack)


# 将列表当作队列使用
# 队列作为特定的数据结构，最先进入队列的元素最先被释放（先进先出），但是效率不高（因为操作头部数据其它的数据都得一个一个移动）
# 先append()再popleft()就可以模拟这一现象
print(10 * '*', '队列', 10 * '*')
from collections import deque
queue = deque(['Java', 'C', 'C++'])
queue.append('Python')
queue.append('C#')
print('释放前：', queue)
queue.popleft()
print('释放后：', queue)
queue.popleft()
print('再释放：', queue)


# 嵌套列表的解析
print(10 * '*', '嵌套列表', 10 * '*')
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


# del语句
# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。
# 与使用 pop() 返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
print(10 * '*', 'del语句', 10 * '*')
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print('移除第一个元素后：', a)
del a[2:4]
print('移除第二三个元素后：', a)
del a[:]
print('移除第所有元素后：', a)
# del a是删除a这个实体变量


# 构建字典的方式
print(10 * '*', 'dict', 10 * '*')
# 固定模式
dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)
# 关键字只是简单的字符串
dict2 = dict(sape=4139, guido=4127, jack=4098)
print(dict2)
# 也可以用任意键值表达式来推导
dict3 = {x: x**2 for x in (2, 4, 6)}
print(dict3)


# 字典遍历的技巧
print(10 * '*', 'dict遍历', 10 * '*')
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))