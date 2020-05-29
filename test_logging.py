import logging
#logging模式
# logging.basicConfig(level=logging.DEBUG,  
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
#                     datefmt='%a, %d %b %Y %H:%M:%S',  
#                     filename='C:/Users/weiyji/Desktop/file/test.log',  
#                     filemode='a')  
# logging.debug('debug message')  
# logging.info('info message')  
# logging.warning('warning message')  
# logging.error('error message')  
# logging.critical('critical message')

#logger模式
logger = logging.getLogger()
fh = logging.FileHandler('test.log')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')