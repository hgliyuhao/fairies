import jieba

def jieba_init():
    
    """
        初始化jieba分词字典 提前加载,不会在调用时再加载
    """
    
    jieba.initialize()

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