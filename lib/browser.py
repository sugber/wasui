from selenium import webdriver
from config.config import *
from logging import *

def open_browses():
    logging.info ( "您选择的是{}浏览器".format ( browser ) )
    if browser == 'Chrome':
        drier = webdriver.Chrome()
    elif browser == 'Firefox':
        drier = webdriver.Firefox()
    elif browser == 'IE':
        drier = webdriver.Ie()
    logging.info ( "{}浏览器启动成功".format ( browser ) )

    drier.get(url)
    logging.info ( "{}地址打开成功".format ( url ) )
    drier.maximize_window()
    logging.info ("将浏览器扩大全屏完成")
    return drier
