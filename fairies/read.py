import os
import csv
import json
from tqdm import tqdm
import xlrd
import numpy as np
import orjson


class ReadData:
    """
    Class to read data from various file formats.
    """

    def __init__(self, fileName, table_name="", isWithTitle=False):
        self.fileName = fileName
        self.table_name = table_name
        self.isWithTitle = isWithTitle
        self.res = []

        ext = os.path.splitext(fileName)[1]
        read_func = {
            '.txt': self.read_txt,
            '.json': self.read_json,
            '.csv': self.read_csv,
            '.xlsx': self.read_excel,
            '.npy': self.read_npy
        }.get(ext)

        if not read_func:
            raise ValueError(
                "The format of the read file can only be JSON, TXT, CSV, XLSX, NPY"
            )

        self.res = read_func()

    def read_txt(self):
        with open(self.fileName, "r", encoding='utf8') as f:
            return [d for d in tqdm(f.readlines())]

    def read_json(self):
        with open(self.fileName, 'r', encoding='utf8') as f:
            try:
                return orjson.loads(f.read())
            except:
                return [json.loads(line) for line in tqdm(f)]

    def read_excel(self):
        data = xlrd.open_workbook(self.fileName)
        table = data.sheet_by_name(
            self.table_name) if self.table_name else data.sheets()[0]
        rowNum = table.nrows
        colNum = table.ncols
        return [[table.cell(i, j).value for j in range(colNum)]
                for i in range(rowNum)]

    def read_csv(self):
        with open(self.fileName, encoding='utf-8') as f:
            return [l for l in tqdm(csv.reader(f))]

    def read_npy(self):
        return np.load(self.fileName, allow_pickle=True).tolist()


def read(fileName, table_name=""):
    return ReadData(fileName, table_name).res