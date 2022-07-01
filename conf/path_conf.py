import os

# 基本路径
basepath = os.path.abspath(os.path.dirname(__file__) + os.path.sep + '..')
# print(basepath)

# 数据驱动的路径：excel的路径
path_excel = os.path.join(basepath, 'data' + os.path.sep + 'test_case.xlsx')
# print(path_excel)

# mysql的配置文件
path_mysql = os.path.join(basepath, 'conf' + os.path.sep + 'conf.ini')
# print(path_mysql)

# 用例所在目录
path_test_data = os.path.join(basepath, 'case' )
# print(path_test_data)

# 报告输出的目录
path_report = os.path.join(basepath, 'report')
print(path_report)