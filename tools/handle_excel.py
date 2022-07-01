from conf.path_conf import path_excel
import openpyxl



class HandleExcel:

    def __init__(self, path_excel):
        # 获取workbook对象
        self.wb = openpyxl.load_workbook(path_excel)


    def read_excel(self, sheet_name):
        """
        读取excel中的所有数据，然后将数据都转变成【{}，{}】
        :param sheet_name:
        :return:
        """
        self.sheet = self.wb[sheet_name]
        if self.sheet:
            # 读取excel中所有的数据
            self.all_data = list(self.sheet.values)
            tamp_list = []
            key = self.all_data[0]
            for i in self.all_data[1:]:
                r = dict(zip(key, i))
                tamp_list.append(r)
            return tamp_list
        else:
            print(f"未找到该表单：{sheet_name}")



    def write_excel(self):
        pass

    def save_excel(self):
        pass

if __name__ == '__main__':
    wb = HandleExcel(path_excel)
    r = wb.read_excel('加入购物车')
    print(r)
    print('-'*50)
    print(type(r))
    h = r[0]
    print(type(r[0]))
    print('-' * 50)
    hh = h['assert_mysql']
    print(type(hh))