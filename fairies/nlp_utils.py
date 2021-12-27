import re
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  

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

def split_to_paragraph(content, filter_length=(2, 1000)):

    """
        拆分成段落
    """
    
    content = re.sub(r"\s*", "", content)
    content = re.sub("([。！…？?!；;])", "\\1\1", content)
    sents = content.split("\1")
    sents = [_[: filter_length[1]] for _ in sents]

    res = []
    temp = ''
    for _ in sents:
        if len(temp + _ ) > filter_length[1]:
            res.append(temp)
            temp = _
        else:
            temp = temp + _
    if len(temp) > 0:
        res.append(temp)

    return res

def split_to_sents(content, filter_length=(2, 1000)):

    """
        拆分成句子
    """
    content = re.sub(r"\s*", "", content)
    content = re.sub("([。])", "\\1\1", content)
    sents = content.split("\1")
    sents = [_[: filter_length[1]] for _ in sents]
    return [_ for _ in sents
            if filter_length[0] <= len(_) <= filter_length[1]]

def split_to_subsents(content, filter_length=(2, 1000)):

    """
        拆分成子句
    """

    content = re.sub(r"\s*", "", content)
    content = re.sub("([。！…？?!；;,，])", "\\1\1", content)
    sents = content.split("\1")
    sents = [_[: filter_length[1]] for _ in sents]
    return [_ for _ in sents
            if filter_length[0] <= len(_) <= filter_length[1]]


def get_slide_window_text(text,maxlen,window):

    """
    使用移动窗口的方式分割text
    基于','分割文本,尽可能保留更多完整的信息,而不是根据字数强行分割
    
    param text 需要处理的文本
          maxlen 分割成文本的最大长度 需要小于1000
          window 滑动窗口长度
    """

    lists = split_to_subsents(text)
    lists_len = [len(i) for i in lists]

    # 在滑动的时候尽量保存完整的信息
    # 找到开始的位置

    start = 0
    sumTemp = 0

    cut_list = []

    for i in range(len(lists_len)):
        if sumTemp + lists_len[i]< maxlen:
            sumTemp += lists_len[i]
        else:
            if len(lists_len) > 1:
                cut_list.append([start,max(i-1,start)])
                sumTemp = sumTemp - lists_len[start]
                start += 1
                while sumTemp > maxlen - window :
                    if start + 1 < i - 1:
                        start += 1
                        sumTemp = sumTemp - lists_len[start]
                    else:
                        start = max(i-1,start)
                        sumTemp = lists_len[start]
                        break
                sumTemp += lists_len[i]

        if i == len(lists_len) -1 :
            cut_list.append([start,i])

    res = [] 

    for i in cut_list:
        new = ''
        for k in range(i[0],i[1]+1):
            new += lists[k]
        res.append(new)    

    return res


def get_cut_window_text(text,maxlen,window):
    
    """
    使用截断的方式分割text
    基于','分割文本,尽可能保留更多完整的信息,而不是根据字数强行分割
    
    param text 需要处理的文本
          maxlen 分割成文本的最大长度 需要小于1000
          window 滑动窗口长度
    """
    textlen = len(text)

    start = 0
    end = maxlen
    lists = []

    while end < textlen:
        lists.append([start,end+1])
        start += window
        end += window

    if start < textlen:
        lists.append([start,textlen])

    res = []

    for i in lists:
        res.append(text[i[0]:i[1]])

    return res