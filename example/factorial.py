# 通过用户输入数字计算阶乘
 
# 获取用户输入的数字
import time
start = time.time()
# num = int(input("请输入一个数字: "))
num = 10000
factorial = 1
 
# 查看数字是负数，0 或 正数
if num < 0:
   print("抱歉，负数没有阶乘")
elif num == 0:
   print("0 的阶乘为 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("%d 的阶乘为 %d" %(num,factorial))

end = time.time()

print('开始毫秒数：', start)
print('结束毫秒数：', end)
print('运行时间：', end - start)