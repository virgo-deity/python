# 高阶函数
# def f(n):
#     return n*n
# def foo(a,b,func):
#     return func(a) + func(b)
# print(foo(3,4,f))

#nonlocal
# def outer():
#     count = 10
#     def inner():
#         nonlocal count
#         count = 20
#         print(count)
#     inner()
#     print(count)
# outer()
#global
# count = 10
# def outer():
#     global count
#     print(count)
#     count = 20
#     print(count)
# outer()

# def f(n):
#     num = 1 
#     for i in range(1,n+1):
#         num = num * i
#     return num
# print(f(5))

# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n-1)
# print(f(900))

# def fibo(n):
#     # if n == 0 or n == 1:
#     #     return 1
#     if n <= 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# print(fibo(10))

#filter
# str = ['a','b','c','d']
# def fun1(s):
#     if s == 'a':
#         return s
# ret = filter(fun1,str)
# print(list(ret))
#map:
# str = ['a','b','c','d']
# def func1(s):
#     return s + 'love'
# ret = map(func1,str)  
# print(list(ret))

#reduce
# from functools import reduce
# def add(x,y):
#     return x+y
# ret = reduce(add,range(1,101))
# print(ret)
# print(reduce(lambda x,y:x*y,range(1,6)))

# def outer():
#     x = 10
#     def inner():
#         print(x)
#     return inner
# # outer()()
# ret = outer()
# ret()
# import time
# def foo():
#     start_time = time.time()
#     print('Are You OK!')
#     time.sleep(2)
#     end_time = time.time()
#     print(f'该程序用了{end_time-start_time}秒')

# foo()
# import time
# def foo():
#     print('foo......')
#     time.sleep(2)
# def bar():
#     print('bar......')
#     time.sleep(3)
# def show_time(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print(f'take {end_time-start_time} to execute...')

# show_time(bar)
# import time
# def logger(flag=''):
#     def show_time(f):
#         def inner(*x,**y):
#             start_time = time.time()
#             f(*x,**y)
#             end_time = time.time()
#             print(f'take {end_time-start_time} to execute...')
#             if flag == 'true':
#                 print('pls record logging...') 
#         return inner
#     return show_time
# @logger('true')
# def foo(*a,**b):
#     sums = 0
#     for i in a:
#         sums+=i
#     print(sums)
#     time.sleep(2)
# foo(1,2,3,4,9)
# @logger()
# def bar(a,b):
#     print(a+b)
# bar(2,5)