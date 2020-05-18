from selenium.webdriver.common.by import By
from config.config import *
from lib.browser import *
from time import *

class mytest():
    def element(self,case):
        sugber = case["sugber"]
        find_type = case.get("find_type")
        driver = self.driver

        if find_type == 'By.ID':
            cc = driver.find_element(By.XPATH,sugber)
        elif find_type == 'By.NAME':
            cc = driver.find_element(By.XPATH,sugber)
        logging.info("定位元素方法是{}方法".format(find_type))
        return cc

    def dongzuo(self,case,dongzuo):
        logging.info("用例执行动作是{}".format(dongzuo))
        if dongzuo == 'click':
            self.element(case).click()
        elif dongzuo == 'send_keys':
            self.element(case).send_keys(case["value"])
        logging.info("用例执行完成")



