# -*- coding: utf-8 -*-
# @Author  : ting.wen
# @Time    : 2022/10/18 10:57 下午
# @Function:
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from email_manage import EmailManage


class TestPrint(unittest.TestCase):
    def test_print_01(self):
        print("print the 01 sentence.")

    def test_print_02(self):
        print("print the 01 sentence.")

    def test_print_03(self):
        print("print the 01 sentence.")

