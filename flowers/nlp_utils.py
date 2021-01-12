import re
import jieba

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

def clean_data(text):

    temp = ['\uf043','\uf020','\uf076','\uf046','\uf075','\uf06c','\uf09f','\uf0d8','\uf072','\uf077','．','…','„',' ']
    List = re.findall(r'[(]cid.*?[)]',text)
    List = List + temp
    for l in List:
        text = text.replace(l,'')
    text = removeLineFeed(text)
    return text            

def removeLineFeed(text):
    """去除换行 tab键"""
    k = text.replace('\r','').replace('\n','').replace('\t',' ')
    return k

def jieba_cut(text):
    
    """
        jieba分词普通模式
        传入text 返回list
    """
    res = []
    seg_list = jieba.cut(text, cut_all=False)
    for i in seg_list:
        res.append(i)

    return res    

def jieba_add_words(lists):
    for i in lists:
        jieba.suggest_freq(i, True)

def isMask(text):
    # 判断该
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