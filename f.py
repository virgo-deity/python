# f=open('poem.txt','r',encoding='utf8')

# print(f.readlines())
# num = 0
# for i in f.readlines():
#     num += 1
#     if num == 3:
#         print(i.strip()+'love')
#     else:
#         print(i.strip())
# print(f.tell())
# num = 0
# for i in f:
#     num += 1
#     if num == 3:
#         i=''.join((i.strip(),'like'))
#     print(i.strip())
# print(f.tell())
# f.close()

# import sys,time
# for i in range(30):
#     sys.stdout.write('*')
#     sys.stdout.flush()
#     time.sleep(0.2)

# f_read = open('poem.txt','r',encoding='utf8')
# f_write = open('poem2.txt','w',encoding='utf8')
# num = 0
# for line in f_read:
#     num += 1
#     if num == 3:
#         line = ''.join([line.strip(),'love\n'])
#         # line = 'love\n'
#     f_write.write(line)
# f_write.close()
# d = {'beijing':{'chaoyang':'yintai'}}
# print(type(d))
# print(d['beijing'])
# s = str(d)
# print(type(s))
# # print(s['beijing'])
# d1 = eval(s)
# print(type(d1))
# print(d1['beijing'])

# with open ('poem.txt','r',encoding='utf8') as f_read,open ('poem2.txt','w',encoding='utf8') as f_write:
#     num = 0
#     for line in f_read:
#         num += 1
#         if num == 3:
#             line = ''.join([line.strip(),'love\n'])
#             # line = 'love\n'
#         f_write.write(line)