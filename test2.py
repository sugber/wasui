from selenium.webdriver.common.by import By
from config.config import *
# from lib.browser import *
from time import *
from lib.jietu import *
from selenium import webdriver

class mytest():
    def mingzi(self,case,dongzuo):
        if dongzuo == 'click':
            jname = '-点击'
            jietuname = case["detail"] + jname
        elif dongzuo == 'send_keys':
            jname = '-输入:'
            jietuname = case["detail"] + jname + "aalue"
        elif dongzuo == 'clear':
            jname = '-清除'
            jietuname = case["detail"] + jname
        # jietuname = case["detail"]+jname+case["value"]
        jietupath = os.path.join(path,"jietu",jietuname+".png")
        return jietupath

    def element(self,case,dongzuo):
        sugber = case["sugber"]
        find_type = case.get("find_type")
        driver = self.driver
        # driver.get_screenshot_as_file(jietus)


        if find_type == 'By.ID':
            cc = driver.find_element(By.XPATH,sugber)
        elif find_type == 'By.NAME':
            cc = driver.find_element(By.XPATH,sugber)
        logging.info("定位元素方法是{}方法".format(find_type))
        return cc

    def dongzuo(self,case,dongzuo):
        logging.info("用例执行动作是{}".format(dongzuo))
        if dongzuo == 'click':
            self.element(case,dongzuo).click()
        elif dongzuo == 'send_keys':
            self.element(case,dongzuo).send_keys(case["value"])
        self.driver.get_screenshot_as_file (self.mingzi(case,dongzuo) )
        logging.info("用例执行完成")
    #

    #
    # def jietu(self,case,dongzuo):
    #     self.drvier.get_screenshot_as_file (self.mingzi(case,dongzuo))


