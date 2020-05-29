import configparser
#生成配置文件
config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9'}
config["beijing"] = {'haidian': '45',
                      'chaoyang': 'yes',
                     'shijingshan': '9'}
config["hebei"] = {'hengshui': '45',
                      'shijiazhuang': 'yes',
                     'baoding': '9'}
# config['bitbucket.org'] = {'User':'hg'}
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'     # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
   config.write(configfile)
#通过read读取配置文件
# config.read('example.ini')
# print(config.sections())
# print(config.defaults())
#通过循环读取文件
# for key in config['bitbucket.org']:
#     print(key)
#删除块section
# config.remove_section('topsecret.server.com')
# config.write(open('example.ini','w'))
#修改键key
# config.set('bitbucket.org','user','weiyji')
# config.write(open('example.ini','w'))
#删除key
# config.remove_option('bitbucket.org','user')
# config.write(open('example.ini','w'))