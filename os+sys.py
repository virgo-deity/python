import os
import sys
print(os.getcwd())
# os.makedirs('abc\\def')#创建多个文件夹
#os.removedirs('abc\\def')#删除多个文件夹，只删除空目录文件夹
# os.mkdir('abc')#创建一个文件夹
# os.rmdir('abc')#删除一个文件夹
# dirs=os.listdir(r'C:\Users\weiyji\Desktop\file')#列出当前目录的内容
# print(dirs)
# os.remove('f.py')#只能删除文件，不能删除文件夹
# os.rename('poem.txt','poem1.txt')#更改文件夹和文件名称
# info=os.stat('login.py')#查询文件大小，断点续传的时候需要用到
# print(info)#st_atime是文件最后被访问的时候，st_mtime是文件最后保存的时间，st_size是查看文件大小
# print(os.sep)
# print(sys.platform)#判断操作系统的版本