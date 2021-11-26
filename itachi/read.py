import os
import csv
import json
from tqdm import tqdm
import xlrd
import xlwt
from xlutils.copy import copy


class read_data():

    def __init__(   
            self,
            fileName,
            table_name = "",
            isWithTitle = False     
                    
        ):
        
        self.fileName = fileName
        self.table_name = table_name
        self.isWithTitle = isWithTitle
        self.res = []

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

        else:
            raise ValueError(
                "The format of the read file can only be JSON, TXT, CSV, XLSX"
            )          

    def read_txt(self):
        
        res = []
        with open(self.fileName, "r" ,encoding='utf8') as f:
            data = f.readlines()
            for d in tqdm(data):
                res.append(d)

        return res

    def read_json(self):
        
        try:
            with open(self.fileName,'r', encoding='utf8') as f:
                json_data = json.load(f)
        except:
            json_data = []
            with open(self.fileName,encoding='utf-8') as f:
                for line in tqdm(f):
                    json_data.append(json.loads(line))        
        return json_data    

    def read_excel(self):
        
        res = []

        data = xlrd.open_workbook(self.fileName)
        table_name =  self.table_name

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
                    row_data.append(table.cell(i,j).value)
                res.append(row_data)   

        return res

    def read_csv(self):
        res = []
        with open(self.fileName,encoding='utf-8') as f:
            reader = csv.reader(f)
            for l in tqdm(reader):
                res.append(l)
        return res        
    
def read(fileName):
    return read_data(fileName).res

