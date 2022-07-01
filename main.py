import json
import pymysql
from jsonpath import jsonpath
from tools.handle_excel import HandleExcel
from conf.path_conf import path_mysql, path_excel, path_test_data, path_report
from tools.handle_data import Data
import re
from random import randint
from configparser import ConfigParser
from tools.handle_db import Handle_Mysql
from unittestreport import TestRunner
import unittest
import time



# 创建测试套件并加载测试用例
suit = unittest.defaultTestLoader.discover(path_test_data, 'test*')

# 创建运行对象
runner = TestRunner(suit, filename='hello_world'+str(time.time()), report_dir=path_report, title='title测试报告', tester='wang', desc="练习生成的报告", templates=2)

# 运行
runner.run()

runner.send_email(host="smtp.qq.com",
                  port=465,
                  user="838054392@qq.com",
                  password="pummkfahmceibfha",
                  to_addrs="838054392@qq.com")




