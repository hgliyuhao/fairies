import xlrd
import xlwt
from xlutils.copy import copy

def read_excel(fileName,table_name):
    # rowNum = table.nrows
    # colNum = table.ncols
    # 使用table.cell(i,0).value 调用
    data = xlrd.open_workbook(fileName)
    table = data.sheet_by_name(table_name)
    return table


def write_excel(fileName,sheet_num = 0):

    """
        通过worksheet写入excel的值
        处理后的excel，
        使用excel.save("final.xls")保存
    
    """

    data = xlrd.open_workbook(fileName)
    excel = copy(data)  # 将xlrd的对象转化为xlwt的对象
    worksheet = excel.get_sheet(sheet_num)  # 获取要操作的sheet
    
    return excel,worksheet