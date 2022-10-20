# -*- coding: utf-8 -*-
# @Author  : ting.wen
# @Time    : 2022/10/19 11:34 下午
# @Function:

import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from email_manage import EmailManage

# 使用加载器去发现当前目录下以 py结尾的文件
suite = unittest.defaultTestLoader.discover("./", "*.py")
file = open("./report.html", "wb")

runner = HTMLTestRunner(stream=file,
                        title="Automated Test Report",
                        description="test report")
runner.run(suite)
file.close()

time.sleep(3)

mng = EmailManage()
mng.send_email(report_name=file.name)

