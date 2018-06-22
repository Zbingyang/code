"""__author__ = 余婷"""

from datetime import *
import time


# ==================date类=================
"""静态方法和字段"""
# date类可以获取的最大日期
print(date.max)

# date类可以获取的最小日期
print(date.min)

# datel类可以表示的最小单位:天，不能处理时分秒
print(date.resolution)

# 获取当日对应的date对象
print(date.today())

# 获取到当前的时间戳
t1 = time.time()
t1 -= 899987889
# 将时间戳转换成对应的date对象
d1 = date.fromtimestamp(t1+899987889)
print(d1)

# 通过年月日创建date对象
d2 = date(2017, 6, 10)
print(d2)

# 通过year、day、month去拿到年月日
print(d2.year)
print(d2.month)
print(d2.day)

# 修改date的年月日(不修改原来的date，通过参数去创建对应的新的date)
d3 = d2.replace(year=2018)
print(d2)
print(d3)

# 返回strut_time
t2 = d3.timetuple()
print(t2)
strt3 = time.strftime('week %w', t2)
print(strt3)

# 1-7对应的是周一-周天
print(d3.isoweekday())

# 以特定的格式返回date对应的字符串
print(d3.strftime('%Y年%m月%d日'))


# 拿到当前时间(包括了年月日，时分秒毫秒)
dt = datetime.now()
print(dt)


# timedelta可以对天、时分秒毫秒进行加减操作
# dt 前一天 （求dt的昨天对应的时间）
dt1 = dt + timedelta(days=-1)
print(dt1)

# dt 前两天
dt2 = dt + timedelta(days=-2)
print(dt2)

dt_1 = date(2008, 3, 1)
dt3 = dt_1 + timedelta(days=-1)
print(dt3)

# 2018.1.1  00:00:00
dt_2 = datetime.strptime('2018-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')
dt4 = dt_2 + timedelta(hours=-1)
print(dt4)


dt_3 = datetime.strptime('2017-12-31 00:00:00', '%Y-%m-%d %H:%M:%S')
dt5 = dt_3 + timedelta(days=10)
print(dt5)


































