import os
import csv
import json
from tqdm import tqdm
import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np
import orjson
import datetime

# import chardet
# from chardet.universaldetector import UniversalDetector

# TODO
# import fairies as fa
# import csv
# from tqdm import tqdm
# import chardet
# from chardet.universaldetector import UniversalDetector

# def get_encoding(file):
#         detector = UniversalDetector()
#         with open(file,'rb') as f:
#             for line in f:
#                 detector.feed(line)
#                 if detector.done:
#                     break
#         detector.close()
#         print(detector.result)
#         # return chardet.detect(f.read(1100))['encoding']

# print(get_encoding("0325_3a_tj.csv"))




class read_data():
    def __init__(self, fileName, table_name="", isWithTitle=False):

        self.fileName = fileName
        self.table_name = table_name
        self.isWithTitle = isWithTitle
        self.res = []
        self.head = {}

        # TODO
        # 判断fileName在不在

        if fileName.endswith('.txt'):
            self.res = self.read_txt()
        elif fileName.endswith('.json'):
            self.res = self.read_json()
        elif fileName.endswith('.csv'):
            self.res = self.read_csv()
        elif fileName.endswith('.xlsx'):
            self.res = self.read_excel()
        elif fileName.endswith('.npy'):
            self.res = self.read_npy()
        else:
            raise ValueError(
                "The format of the read file can only be JSON, TXT, CSV, XLSX, NPY"
            )

    def read_txt(self):

        res = []
        with open(self.fileName, "r", encoding='utf8') as f:
            data = f.readlines()
            for d in tqdm(data):
                res.append(d)

        return res

    # def read_json(self):

    #     try:
    #         with open(self.fileName,'r', encoding='utf8') as f:
    #             json_data = json.load(f)
    #     except:
    #         json_data = []
    #         with open(self.fileName,encoding='utf-8') as f:
    #             for line in tqdm(f):
    #                 json_data.append(json.loads(line))
    #     return json_data

    def read_json(self):

        try:
            with open(self.fileName, 'rb') as f:
                json_data = orjson.loads(f.read())
            return json_data
        except:

            try:
                with open(self.fileName, 'r', encoding='utf8') as f:
                    json_data = json.load(f)
            except:
                json_data = []
                with open(self.fileName, encoding='utf-8') as f:
                    for line in tqdm(f):
                        json_data.append(json.loads(line))
            return json_data

    def read_excel(self):

        res = []

        data = xlrd.open_workbook(self.fileName)
        table_name = self.table_name

        if table_name != "":
            table = data.sheet_by_name(table_name)
        else:
            table = data.sheets()[0]

        rowNum = table.nrows
        colNum = table.ncols

        if self.isWithTitle:

            # TODO
            pass
            # title_lists = []
            # for j in range(colNum):
            #     title_lists.append(table.cell(0,j).value)

        else:
            for i in range(rowNum):
                row_data = []
                for j in range(colNum):
                    row_data.append(table.cell(i, j).value)
                res.append(row_data)

        return res

    def read_csv(self):
        res = []
        with open(self.fileName, encoding='utf-8') as f:
            reader = csv.reader(f)
            for l in tqdm(reader):
                res.append(l)
        return res

    def read_npy(self):

        dict_load = np.load(self.fileName, allow_pickle=True)
        return dict_load.tolist()


def read(fileName,table_name=""):

    if table_name == "":
        return read_data(fileName).res
    else:
        return read_data(fileName,table_name).res


def read_json(filename):

    try:
        with open(filename, 'r', encoding='utf8') as f:
            json_data = json.load(f)
        return json_data
    except:
        json_data = []
        with open(filename, encoding='utf-8') as f:
            for line in tqdm(f):
                json_data.append(json.loads(line))
        return json_data


def read_txt(fileName):
    """
        读取txt文件
    """

    res = []
    with open(fileName, "r", encoding='utf8') as f:
        data = f.readlines()
        for d in tqdm(data):
            res.append(d)

    return res


def read_csv(fileName):
    res = []
    with open(fileName, encoding='utf-8') as f:
        reader = csv.reader(f)
        for l in tqdm(reader):
            res.append(l)
    return res


def read_npy(fileName):

    dict_load = np.load(fileName, allow_pickle=True)
    return dict_load.tolist()


def read_orjson(fileName):

    with open(fileName, 'rb') as f:
        json_data = orjson.loads(f.read())
    return json_data