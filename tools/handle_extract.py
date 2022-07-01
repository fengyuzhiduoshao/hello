from jsonpath import jsonpath
from tools.handle_excel import HandleExcel
from conf.path_conf import path_excel
from tools.handle_data import Data



def handle_extract(resp_data, exprs):
    """
    将响应的数据，设置成全局变量
    :param resp_data: 响应数据
    :param exprs: 从excel中，提取的表达式，传入的是字符串类型
    :return:
    """
    # 将excel的表达式转化成字典
    exprs_dict = eval(exprs)
    for key, value in exprs_dict.items():
        actual_data = jsonpath(resp_data, value)

        if actual_data:
            setattr(Data, key, actual_data[0])
        else:
            print("没有提取到数据，提取结果为{}".format(actual_data))

if __name__ == '__main__':
    resp = {'status': 1, 'msg': '加入购物车成功'}
    ex = str({"status":"$.status","msg":"$.msg"})
    print(type(resp), type(ex))

    handle_extract(resp, ex)
    print(Data.status,Data.msg)










