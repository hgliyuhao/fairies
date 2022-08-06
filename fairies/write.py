import json
import codecs
import numpy as np
from tqdm import tqdm
import csv
import orjson


def write_json(filename,res,isIndent = False, isLine = False):
    
    if not isLine and (isinstance(res,dict) or isinstance(res,list)):
        if isIndent:
            json_str = json.dumps(res,ensure_ascii=False,indent=4)
            with open(filename, 'w',encoding = 'utf-8') as json_file:
                json_file.write(json_str)
        else:
            json_str = json.dumps(res,ensure_ascii=False)
            with open(filename, 'w',encoding = 'utf-8') as json_file:
                json_file.write(json_str)
    else:        
        with codecs.open(filename, 'w', 'utf-8') as f:
            for formatted_instance in res:
                json_str = json.dumps(formatted_instance, ensure_ascii=False)
                f.write(json_str)
                f.write('\n')
        f.close()

def write_orjson(fileName,res):
    with open(fileName, 'wb') as json_file:
        json_str = orjson.dumps(res)
        json_file.write(json_str)
    json_file.close()

def write_txt(fileName,lists,model = 'normal'):

    """
        按行写入
    """

    if model == 'normal':
        f = open(fileName,'w', encoding='utf8')
    else:    
        f = open(fileName,'a', encoding='utf8')
    for i in tqdm(lists):
        f.write(str(i))
        f.write('\n')
    f.close()

def write_npy(fileName,lists):

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