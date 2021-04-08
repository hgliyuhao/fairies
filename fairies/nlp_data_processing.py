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