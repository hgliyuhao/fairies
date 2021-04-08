import re

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