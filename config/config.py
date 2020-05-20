import os
import logging
import datetime

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


testpath = os.path.join(path,"test_case")

report_file = os.path.join(path,'report', 'report.html')  # 也可以每次生成新的报告
# log = os.path.join(path,'log', 'log.text')


# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '13166661519@163.com'
smtp_password = 'OQPCJZPTVDJGEGWI'

sender = smtp_user  # 发件人
receiver = 'chengyongda@woaizuji.com'  # 收件人
subject = 'UI自动化测试报告'  # 邮件主题
