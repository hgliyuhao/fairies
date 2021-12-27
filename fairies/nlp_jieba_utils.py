import jieba
from fairies import knowledge
stop_words = knowledge.get_stop_word()


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


def find_co_occurrence_word(texts,nums = 10):

    """
        texts 切分的文本列表
        nums 关键词数量 默认为10
    """

    res = {}
    for text in texts:
        word_lists = jieba_cut(text)
        for word in word_lists:
            if word not in stop_words and len(word) > 1:
                if word not in res:
                    res[word] = 1
                else:
                    res[word] += 1

    res = sorted(res.items(),key=lambda item:item[1],reverse = True)

    pos = []
    for i in res[:nums]:
        pos.append(i[0])

    count = 0
    for text in texts:
        for n in pos:
            if n in text:
                count += 1
                break
    
    print('关键词列表',pos)
    print('覆盖率',count/len(texts))        
    
    return pos