from lib.implement import *
import unittest
from lib.read_execel import *
from time import *
from config.config import *


class CCC ( unittest.TestCase, mytest,Execel ) :
    def __init__(self):
        self.data_list = self.get_execel(datafile,sheet)

    def ccc(self, testname, dongzuo) :
        case = self.get_data (self.data_list, testname )
        print(case)
        logging.info("即将执行用例{}".format(testname))
        self.dongzuo ( case, dongzuo )
        sleep ( 1 )

c = CCC()
print(c.ccc("test_1", 'click'))