import xlrd
from config.config import *

class Execel():
    def get_execel(self,datafile,sheet):
        logging.info("用例地址是{}，sheet页是{}".format(datafile,sheet))
        data_list = []
        sh = xlrd.open_workbook(datafile)
        logging.info("打开文件正常")
        sh = sh.sheet_by_name(sheet)
        logging.info("打开{}页正常".format(sheet))
        wb = sh.row_values(0)
        for i in range(1,sh.nrows):
            d = dict(zip(wb,sh.row_values(i)))
            data_list.append(d)
        return data_list

    def get_data(self,data_list, caseid):
        # data_list = self.get_execel(datafile,sheet)
        for case in data_list:
            if case["caseid"] == caseid:
                return case

