import unittest
from config.config import *
from lib.send_email import *
from lib.HTMLTestReportCN import *


logging.info("================================== 测试开始 ==================================")

discover = unittest.defaultTestLoader.discover(testpath, pattern="testcase.py")


with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="warehousee Test", description="测试描述").run(discover)


send_email(report_file)  # 从配置文件中读取

logging.info("================================== 测试结束 ==================================")