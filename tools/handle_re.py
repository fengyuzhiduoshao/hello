import json

from jsonpath import jsonpath
from tools.handle_excel import HandleExcel
from conf.path_conf import path_excel
from tools.handle_data import Data
import re
from random import randint



# 【{}，{}】，格式为list
# data = HandleExcel(path_excel).read_excel('加入购物车')
# print(type(data))
# #
# data = json.dumps(data)
# print(data)




def handle_req_data(re_data):
    """
    将标识符进行替换
    :param re_data: 格式为字典
    :return: 返回的数据是：dict
    """

    req_data = json.dumps(re_data)
    if re_data :
        # 提取出来是一个列表
        req_data_list = re.findall('#(\w+)#', req_data)
        # 遍历列表，并进行替换
        for i in req_data_list:
            # 判断，如果i==goods_id，那么将goods_id进行替换
            # 替换的时候，要old_data与new_data都必须是字符串
            if i == 'goods_id':
                random_str = str(random())
                req_data = req_data.replace(f"#{i}#", random_str)
    return json.loads(req_data)


# 获取随机数
def random():
    return randint(1,100)

if __name__ == '__main__':
    a = random()
    print(a)
    a = {"goods_id":"#goods_id#", "prom_id":"#prom_id#"}
    hh = handle_req_data(a)
    print(hh, type(hh))
    print('-'*50)
    # hh = json.loads(hh)
    # print(hh)












