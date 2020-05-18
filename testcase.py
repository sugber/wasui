# -*- coding: utf-8 -*-
from lib.casefangfa import *
from lib.browser import *
from time import sleep


class TestWareHouse (CCC,unittest.TestCase) :
    @classmethod
    def setUpClass(self) :
        self.driver = open_browses ()
        sleep ( 3 )

    def test_1(self) :
        self.ccc ( "test_1", 'click' )
        self.ccc ( 'test_1', 'clear' )
        self.ccc ( 'test_1', 'send_keys' )

    def test_2(self) :
        self.ccc ( "test_2", 'click' )
        self.ccc ( 'test_2', 'clear' )
        self.ccc ( 'test_2', 'send_keys' )

    def test_3(self) :
        self.ccc ( "test_3", 'click' )

    def test_4(self) :
        self.ccc ( "test_4", 'click' )

    def test_5(self) :
        self.ccc ( "test_5", 'click' )

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()