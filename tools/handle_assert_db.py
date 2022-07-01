import json
import pymysql
from jsonpath import jsonpath
from tools.handle_excel import HandleExcel
from conf.path_conf import path_mysql, path_excel
from tools.handle_data import Data
import re
from random import randint
from configparser import ConfigParser
from tools.handle_db import Handle_Mysql

"""
1、连接数据库
2、创建游标
3、关闭游标、关闭连接
"""

# a = '{"sql":"SELECT count(*) from tp_cart WHERE goods_id=210;","expect":1}'
#
# b = {'a':{"sql":"SELECT count(*) from tp_cart WHERE goods_id=210;","expect":1}}
# print(b['a'])
# print(type(b['a']))


def assert_db(sql, expect):
    # 执行sql，用查询的结果和预期值做一个比较
    # 提取sql
    try:
        a = Handle_Mysql(path_mysql)
        b = a.get_count(sql)
        assert b == expect
    except:
        return False
    finally:
        a.close_mysql()
    return True


if __name__ == '__main__':
    a = {"sql":"SELECT count(*) from tp_cart WHERE goods_id=210;","expect":1}
    b = assert_db(a['sql'], 2)
    print(b)


