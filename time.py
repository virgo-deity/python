# import time
# import datetime

# print(help(time))#打印time帮助信息
# print(time.gmtime())#打印结构化时间
# print(time.localtime())#打印本地时间
# struct_time=time.localtime()#用变量接收本地时间
# print(time.strftime('%Y--%m--%d %H:%M:%S',struct_time))#根据localtime打印自定义结构时间格式

#通过给定的一个时间转换为结构化时间，然后取特定的年月日和时分秒
# print(time.strptime('2020--05--05 16:26:13','%Y--%m--%d %H:%M:%S'))
# #time.struct_time(tm_year=2020, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=26, tm_sec=13, tm_wday=1, tm_yday=126, tm_isdst=-1)
# a = time.strptime('2020--05--05 16:26:13','%Y--%m--%d %H:%M:%S')
# print(a.tm_year)
# print(a.tm_mon)
# print(a.tm_mday)

# print(time.ctime(2000000000))#通过特定时间戳转换成格式化时间
# print(time.mktime(time.localtime()))#通过本地时间转换为时间戳格式
# print(datetime.datetime.now())#datetime模块里取当前时间

import random
# def v_code():
#     code = ''
#     for i in range(5):
#         add=random.choice([random.randrange(10),chr(random.randrange(65,90))])
#         code+=str(add)
#     print(code)
# v_code()
print(random.random())#生成一个浮点型随机数
print(random.randint(1,10))#生成随机整数，含8
print(random.randrange(1,8))#生成随机数，不含8
print(random.choice('helloworld'))#随机选一个字符
print(random.choice(['123',4,[1,2]]))#随机选1个
print(random.sample(['123',4,[1,2]],2))#随机选2个


