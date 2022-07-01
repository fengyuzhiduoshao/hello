import json
import unittest
from unittestreport import ddt, list_data
from conf.path_conf import path_excel
from tools.handle_data import Data
from tools.handle_excel import HandleExcel
from tools.handle_api import Handle_Api
from tools.handle_extract import handle_extract
from tools.handle_re import handle_req_data


data = HandleExcel(path_excel).read_excel('加入购物车')  #[{},{}]
# print(data)





@ddt
class TestCart(unittest.TestCase):

    @list_data(data)
    def test_add_shopping_cart(self, case):
        """

        :param case: 传入的是字典格式
        :return:
        """
        # print(case['req_data'])
        data = case['req_data'] # str
        data = eval(handle_req_data(data))   # 将标识符进行替换
        # print(headers)
        res = Handle_Api().api(method=case['method'], url=case['url'], data=data, headers=eval(case['headers']))
        # res = json.loads(res)
        # print(type(res))
        print(res.json())
        print(type(res.json()))
        hh = case['extract']
        print(hh, type(hh))
        # 将响应结果提取，并设置成全局变量
        handle_extract(res.json(), hh)
        self.assertEqual(1, res.json()['status'])


