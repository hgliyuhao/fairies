import re
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  

def text_len_analysis(texts):
    
    """
    可视化文本长度
    param texts 需要分析的文本数组
    
    """

    length = []

    for i in texts:
        length.append(len(i))
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.hist(length, bins=10, color='blue', alpha=0.7)
    plt.show()

def dict_bar(dicts):

    # TODO 元素太多标签看不清

    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 字典转元组
    x = tuple(dicts)
    y = tuple(dicts.values())

    plt.bar(x, y, width= 1)
    plt.show()


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