import re
# ret = re.findall('a.','abbbbb')
# print(ret)
# ret = re.findall('^a','babcde')
# print(ret)
# ret = re.findall('a$','cedfgab')
# print(ret)
# ret = re.findall('ac*','abcddefadjefdeadedefac')
# print(ret)
# ret = re.findall('a+b','acefddfbdedsabdle')
# print(ret)
# ret = re.findall('c+e','cedjfjfcccejdhfhe')
# print(ret)
# ret = re.findall('a?c','cdefdacgefdaaaac')
# print(ret)
ret = re.findall('a{1,}c','aaaaacdefdg')
print(ret)
#结论
#.匹配一个字符
#^匹配起始位置
#$匹配结束位置
#*匹配（0-正无穷）个字符
#+匹配（1-正无穷）个字符
# ?匹配（0-1）个字符
# {1，3}匹配（1-3）个字符
# {1，}匹配（1-正无穷）个字符