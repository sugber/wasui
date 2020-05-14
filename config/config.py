import os
import logging

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
datafile = os.path.join(path,"data","waseUI.xlsx")
sheet = 'Sheet1'
logpath = os.path.join(path,"log","log.text")

browser = 'Chrome'

url = 'http://warehouse.test.com/index.html'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(funcName)s %(filename)s %(lineno)d %(message)s',
    datefmt= '%y-%m-%d %H:%M:%S',
    filename= logpath,
    filemode= 'a'
)