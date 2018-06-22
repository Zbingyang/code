"""__author__ = 余婷"""

import time


#

# 1.获取时间戳
# t1时间戳  表示的是当前时间到1970.1.1 00：00：00的时间差，单位是秒
# 为什么做服务器的时候存储时间需要存储时间对应的时间戳：
# 1.节约存储空间（一个浮点数的大小8个字节或者16个字节，字符串中的一个字符是2个字节）
# 2.可以对时间进行间接加密
t1 = time.time()
print(t1)

# 2.获取当前的本地时间（struct_time）
t2 = time.localtime()
print(t2)
# 获取年
print(t2.tm_year)
# 获取月
print(t2.tm_mon)
# ?  tm_wday=4


# 3.格式时间转换成struct_time
t3 = time.strptime('2011年9月10号', '%Y年%m月%d号')
print(t3)
print('2011年9月10号是2011年的%d'%t3.tm_yday)


t4 = time.strptime('2010-9-1 10:20', '%Y-%m-%d %H:%M')
print(t4)

t5 = time.strptime('今天是2018年6月1日', '今天是%Y年%m月%d日')
print(t5)

t6 = time.strptime('今天是2018年7月1日', '今天是%Y年%m月%d日')
print(t6)

# 4.将struct_time转换成格式时间
t7 = time.strftime('%Y-%m-%d 周%w', t6)
print(t7)

t8 = time.strftime('%b %d', t6)
print(t8)

































