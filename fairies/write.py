import json
import codecs
import numpy as np
from tqdm import tqdm
import csv
import orjson
import xlsxwriter

def write_json(filename, res, isIndent=False, isLine=False):

    if not isLine and (isinstance(res, dict) or isinstance(res, list)):
        if isIndent:
            json_str = json.dumps(res, ensure_ascii=False, indent=4)
            with open(filename, 'w', encoding='utf-8') as json_file:
                json_file.write(json_str)
        else:
            json_str = json.dumps(res, ensure_ascii=False)
            with open(filename, 'w', encoding='utf-8') as json_file:
                json_file.write(json_str)
    else:
        with codecs.open(filename, 'w', 'utf-8') as f:
            for formatted_instance in res:
                json_str = json.dumps(formatted_instance, ensure_ascii=False)
                f.write(json_str)
                f.write('\n')
        f.close()


def write_orjson(fileName, res):
    with open(fileName, 'wb') as json_file:
        json_str = orjson.dumps(res)
        json_file.write(json_str)
    json_file.close()


def write_txt(fileName, lists, model='normal'):
    """
        按行写入
    """

    if model == 'normal':
        f = open(fileName, 'w', encoding='utf8')
    else:
        f = open(fileName, 'a', encoding='utf8')
    for i in tqdm(lists):
        f.write(str(i))
        f.write('\n')
    f.close()


def write_npy(fileName, lists):
    """
        按行写入
    """

    np.save(fileName, lists)


def write_csv(filename, data):
    """
        将数组的内容写到csv中
        data格式：
            data = [
                        ['class','name','sex','height','year'],
                        [1,'xiaoming','male',168,23],
                        [2,'xiaohong','female',162,22],
                        [3,'xiaozhang','female',163,21],
                        [4,'xiaoli','male',158,21]
                    ]
    :param filename: 需要写入的csv文件路径
    :param data:数组格式的文件内容
    """
    f = open(filename, 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for i in tqdm(data):
        writer.writerow(i)
    f.close()

def write_excel(filename, data, sheet_name='Sheet1'):
    """
    将数据写到excel中， 默认sheet_name='Sheet1'， 可以自行设置
    支持两种数据格式：
            [[line1_cell1, line1_cell2], [line2_cell1, line2_cell2], ...]
        例如：
            [
                ['class','name','sex','height','year'],
                [1,'xiaoming','male',168,23],
                [2,'xiaohong','female',162,22],
                [3,'xiaozhang','female',163,21],
                [4,'xiaoli','male',158,21],
                ...
            ]

        
    :param filename: 需要写入的excel文件路径， 如'a.xlsx'
    :param data: 需要写入的数据
    :param sheet_name: sheet的名称， 默认为：Sheet1
    """

    workbook = xlsxwriter.Workbook(filename)  # 创建一个excel文件
    worksheet = workbook.add_worksheet(sheet_name)  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
    
    write_data = data

    if len(write_data) > 0:
        for i in range(len(write_data)):
            for j in range(len(write_data[i])):
                worksheet.write(i, j, write_data[i][j])

    workbook.close()
