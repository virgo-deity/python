# username= 'root'
# passwd= '123'
# count=0
# print('请登录 >>>>>>>>>')
# while True:
#     user=input('登录名：')
#     pwd=input('密码：')
#     if user == username and pwd == passwd:
#         print('登录成功！欢迎登录！')
#         break
#     else:
#         count +=1
#         print('密码错误！登录失败！',count)
#         if count ==3:
#             break
# userinfo={
#     'root': {'username': 'root',
#               'passwd': '123'},
#     'lee' : {'username': 'lee',
#               'passwd': '10086'},
#     'zhang':{'username': 'zhang',
#               'passwd': '10010'}
#         }

# count=0
# print('请登录 >>>>>>>>>')
# while True:
#     user=input('登录名：').strip()
#     pwd=input('密码：').strip()
#     if user == userinfo[user]['username'] and pwd == userinfo[user]['passwd']:
#         print('登录成功！欢迎登录！')
#         break
#     else:
#         count +=1
#         print('密码错误！登录失败！')
#         if count ==3:
#             break

# def f(n):
#     return n*10

# a = [f(x) for x in range(10)]
# print(a)

# def fib(max):
#     n,before,after = 0,0,1
#     while n < max:
#         # print(before)
#         yield before
#         before,after=after,before+after
#         n = n + 1
# g = fib(10)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g))
# def bar():
#     print('ok1')
#     count=yield 1
#     print(count)

#     yield 2
# b = bar()
# next(b)
# ret=b.send('eeeee')
# import time
# def consumer(name):
#     print('%s 准备吃包子了！' %name)
#     while True:
#         baozi = yield
#         print('包子[%s]来了，被[%s]吃了'%(baozi,name))

# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print('老子开始吃包子了！')
#     for i in range(10):
#         time.sleep(1)
#         print('[%s]做了2个包子！'%name)
#         c.send(i)
#         c2.send(i)
# producer('alex')

# l = [1,2,3,4]
# d=iter(l)
# print(next(l))

# d=max(len(x.strip()) for x in open('poem2.txt','r',encoding='utf8'))
# print(d)

# def add(s, x):
#  return s + x
 
# def gen():
#  for i in range(4):
#   yield i
 
# base = gen()
# for n in [1, 10]:
#  base = (add(i, n) for i in base)
 
# print(list(base))

# def fab(max): 
#     n, a, b = 0, 0, 1 
#     while n < max: 
#         yield b
#         a, b = b, a + b 
#         n = n + 1
# for n in fab(5):
#     print(n)