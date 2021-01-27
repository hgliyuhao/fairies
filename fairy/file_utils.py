import json
import os
import requests
import zipfile
import pandas as pd




def write_json(filename,res):
    json_str = json.dumps(res,ensure_ascii=False,indent=4)
    with open(filename, 'w',encoding = 'utf-8') as json_file:
                    json_file.write(json_str) 

def read_json(filename):
    try:
        with open(filename,'r',encoding='utf8') as f:
            json_data = json.load(f)
    except:
        json_data = []
        with open(filename,encoding='utf-8') as f:
            for line in f:
                json_data.append(json.loads(line))        
    return json_data

def write_txt(fileName,lists,model = 'normal'):

    """
        按行写入
    """
    if model == 'normal':
        f = open(fileName,'w',encoding='utf8')
    else:    
        f = open(fileName, 'a',encoding='utf8')
    for i in lists:
        f.write(str(i))
        f.write('\n')
    f.close()

def read_txt(fileName):

    """
        读取txt文件
    """

    res = []
    file = open(fileName,encoding='utf8') 
    lines = file.readlines(100000)
    for line in lines:
        res.append(line)

    file.close()
    return res

def reSort(filename,isReverse = True):
    
    """
        对字典或数组重新排序,
        isReverse 默认为true 默认越长的元素排在前面 为False 相反 
    """
    
    a = read_json(filename)
    a.sort(key=lambda a: len(a),reverse = isReverse)
    write_json(filename,a)

def get_file_size(fileName):
    # 获取文件大小
    return os.path.getsize(fileName)

def get_file_list(file_path):
    # 获取文件列表
    return os.listdir(file_path)

def download_pdf(fileName):
    # 下载pdf
    requests_pdf_url = fileName
    r = requests.get(requests_pdf_url)
    filename = fileName.replace('http://','').replace('/','')
    with open(filename, 'wb+') as f:
        f.write(r.content)

def unzip_file(zip_src, dst_dir):
       
    """
        解压文件
    """
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)       
    else:
        print('This is not zip')

def an_garcode(dir_names):

    """anti garbled code"""
    os.chdir(dir_names)

    for temp_name in os.listdir('.'):
        try:
            #使用cp437对文件名进行解码还原
            new_name = temp_name.encode('cp437')
            #win下一般使用的是gbk编码
            new_name = new_name.decode("gbk")
            #对乱码的文件名及文件夹名进行重命名
            os.rename(temp_name, new_name)
            #传回重新编码的文件名给原文件名
            temp_name = new_name
        except:
            #如果已被正确识别为utf8编码时则不需再编码
            pass      


def get_listdir(path):
    
    """
        得到文件下路径
    """

    res = []
    a = os.listdir(path)
    for i in a:
        k = os.path.join(path,i)
        res.append(k)

    return k    