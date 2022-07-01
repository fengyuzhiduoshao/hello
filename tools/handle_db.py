import json
import pymysql
from jsonpath import jsonpath
from tools.handle_excel import HandleExcel
from conf.path_conf import path_mysql, path_excel
from tools.handle_data import Data
import re
from random import randint
from configparser import ConfigParser

"""
1、连接数据库
2、创建游标
3、关闭游标、关闭连接
"""


class Handle_Mysql:

    def __init__(self, conf_mysql_data):
        """

        :param conf_mysql_data: mysql的配置文件
        """
        try:
            # 创建一个连接信息
            conf = ConfigParser()
            conf.read(conf_mysql_data)
            print(conf.get('mysql', 'user'))
            self.conn = pymysql.connect(
                user=conf.get('mysql', 'user'),
                passwd=conf.get('mysql', 'passwd'),
                port=int(conf.get('mysql', 'port')),
                host=conf.get('mysql', 'host'),
                cursorclass=eval(conf.get('mysql', 'cursorclass')),
                database=conf.get('mysql', 'database')
            )
            self.cursor = self.conn.cursor()
        except Exception as e:

            raise print(f"异常为：{e}")

    def get_count(self, sql):
        """
        获取sql的数据条数
        :param sql: 执行sql
        :return: 数据条数
        """
        count = self.cursor.execute(sql)
        return count

    def read_mysql(self, sql, size):
        """
        获取查询的数据
        :param sql:执行的sql
        :param size: 要返回的条数
        :return: 返回查询的数据
        """
        try:
            a = self.get_count(sql)
            if size == -1:
                res = self.cursor.fetchall()
            elif size == 1:
                res = self.cursor.fetchone()
            elif size > 1:
                res = self.cursor.fetchmany(size)
        except Exception as e:
            raise e

        return res


    def update_mysql(self, sql):
        """
        对数据库进行：增，删，改的操作，一定要记得，提交，否则不能保存修改后的数据
        :param sql: 执行的sql
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("执行成功！！！")
        except Exception as e:
            self.conn.rollback()
            raise print(f"抛出异常：{e}")



    def close_mysql(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    a = Handle_Mysql(path_mysql)
    b = a.read_mysql('SELECT * from tp_goods   LIMIT 10;', -1)
    print(b)
    c = a.update_mysql('UPDATE tp_goods SET market_price=199 WHERE goods_id=1;')
    a.close_mysql()