import re
import jieba
import random
import datetime

def isMask(text):
    
    # 判断该字符是否是标点符号
    mask_list = ["。","！","…","？","?","!","；",";","，"]
    if text in mask_list:
        return True
    else:
        return False   

def isHasMark(text):
    
    # 判断文本中是否有符号
    marks = ['。','！','…','？','?','!','；',';','，']

    for i in marks:
        if i in text:
            return True

    return False

def label2id(labels):
    """
    return: id2label,label2id 
    """

    id2label = dict(enumerate(labels))
    label2id = {j: i for i, j in id2label.items()}
    return id2label,label2id      

def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False

def find_lcs(s1, s2):
    """find the longest common subsequence between s1 ans s2"""
    """公共子串"""
    m = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    max_len = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i+1][j+1] = m[i][j]+1
                if m[i+1][j+1] > max_len:
                    max_len = m[i+1][j+1]
                    p = i+1
    return s1[p-max_len:p], max_len    

def random_build_data(all_data,percent):
    
    """
        检查整个字符串是否包含中文
        :param all_data: list 全部数据
        :param percent: int 按照1：percent分配train_data和dev_data
                        0.9 代表train_data和dev_data 比例 9:1
        :return: train_data,dev_data
    """
    random.shuffle(all_data)

    if percent < 1:
        percent = int(1/(1-percent))
        if percent > 1:
            percent -= 1

    train_data = [d for i, d in enumerate(all_data) if i %percent != 0]
    dev_data = [d for i, d in enumerate(all_data) if i %percent == 0]

    return train_data,dev_data

def get_data_information(): 

    """
        获得时间信息
    """

    cur=datetime.datetime.now()
    day = cur.day
    month = cur.month
    return day + '_' + month


def long_substr(data):
    
    """
        输入数组,输出多个字符传的公共子串
    """
    
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True        