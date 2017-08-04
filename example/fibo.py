'''
# Python 斐波那契数列实现
 
# 获取用户输入数据
nterms = int(input('How many?'))

# 第一和第二项
n1 = 0
n2 = 1
count = 2

if nterms <= 0:
    print('Positive number allowed!')
if nterms == 1:
    print("Fibo:")
    print(n1)
else:
    print("Fibo:")
    print(n1, ',' , n2, end=' , ')
    while count < nterms:
        nth = n1 + n2
        print(nth, end=' , ')
        n1 = n2
        n2 = nth
        count += 1
'''


# 递归方法
def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input('How many?'))
if n <= 0:
    print('Positive number allowed!')
else:
    print('fibo:', end=' , ')
    for i in range(n):
        print(fibo(i), end=' , ')








