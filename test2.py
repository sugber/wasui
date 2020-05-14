import xlrd
from config.config import *

@classmethod
def get_execel(datalife,sheet):
    logging.info("用例地址是{}，sheet页是{}".format(datalife,sheet))
    data_list = []
    sh = xlrd.open_workbook(datalife)
    logging.info("打开文件正常")
    sh = sh.sheet_by_name(sheet)
    logging.info("打开{}页正常".format(sheet))
    wb = sh.row_values(0)
    for i in range(1,sh.nrows):
        d = dict(zip(wb,sh.row_values(i)))
        data_list.append(d)
    return data_list

def get_data(caseid):
    data_list = get_execel(datafile,sheet)
    for case in data_list:
        if case["caseid"] == caseid:
            return case

if __name__ == '__main__':
    data_list = get_execel(r"C:\Users\dell\PycharmProjects\wasui\waseUI.xlsx", "Sheet1")
    case = get_data(data_list,"test_1")
    print(case)