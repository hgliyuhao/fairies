import re
import json
from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import os
from fairies.nlp_utils import clean_data
from fairies.nlp_utils import isHasMark
from fairies.nlp_utils import split_to_sents
from fairies.nlp_utils import removeLineFeed
from bs4 import BeautifulSoup
from fairies import prefix

prefix_list = prefix.prefix

def isHasPrefix(text):

    for i in prefix_list:
        if i in text:
            return True
    return False   

def read_pdf_by_line(filename):

    """
    read pdf by line

    """
    with open(filename, "rb") as pdf:
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)
            process_pdf(rsrcmgr, device, pdf)
            device.close()
            content = retstr.getvalue()
            retstr.close()
            lines = str(content).split("\n")
    return lines

def read_pdf_by_box(pdf):

    praser = PDFParser(open(pdf, 'rb'))
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)

    doc.initialize()

    if not doc.is_extractable:
        return []
    else:

        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        res = []
        nums = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']

        for page in doc.get_pages():

            interpreter.process_page(page)                        
            layout = device.get_result()
            
            temp_label = ''   # 段落标签
            is_merge = False  # 针对pdf的分页

            for x in layout:
                if isinstance(x, LTTextBox):

                    text = x.get_text().strip()

                    if text in nums:
                        is_merge = True
                        continue
                    # print(text)
                    if len(text) < 2:
                        continue
                    
                    if is_merge :
                        is_merge = False
                        if len(res) > 0:
                            res[-1][1] = res[-1][1] + clean_data(text) 
                        temp_label = ''
                        continue

                    if text[0] in nums and text[1] == '.':
                        start = 1
                        for i in range(1,len(text)-1):
                            if text[i] in nums or text[i] == '.':
                                start = i  
                            else:
                                break
                        temp_label = ''
                        text = text[start+1:]   
                    
                    if text == '':
                        continue

                    if len(text) < 18 and not isHasMark(text):

                        temp_label = text

                    if '    ' in text:
                        s = text.find('     ')
                        temp_label = text[:s]

                        text = text[s:]

                    if len(text) > 18 or text[-1] == '。':
                        temp_label = clean_data(temp_label)
                        text = clean_data(text)

                        if isHasMark(temp_label) or len(temp_label) > 25:
                            res.append(['', temp_label + text])
                        else:
                            res.append([temp_label,text])
                        temp_label = ''


        texts_only = []
        texts_with_title = []

        isStart = True
        temp = ''
        temp_title = ''

        for k in res :
            if isStart :
                  
                if k[0] != '':
                    if k[1][-1] == '。':
                        temp = temp + k[1]
                        temp = clean_data(temp)
                        temp_title = temp_title + k[0]

                        texts_with_title.append([temp_title,temp])

                        temp_list = split_to_sents(temp,(2,128))
                        for t in temp_list:
                            texts_only.append(t)
                        
                        # reset
                        
                        temp = ''
                        temp_title = ''      
                        isStart = False
                    else:
                        temp = temp + k[1]
                        temp_title = temp_title + k[0]

                if k[0] == '':
                    if k[1][-1] == '。':
                        temp = temp + k[1]
                        temp = clean_data(temp)
                        temp_title = temp_title
                        texts_with_title.append([temp_title,temp])

                        temp_list = split_to_sents(temp,(2,128))
                        for t in temp_list:
                            texts_only.append(t)
                        
                        # reset
                        
                        temp = ''
                        temp_title = ''      
                        isStart = False
                    else:
                        temp = temp + k[1]
                        temp_title = temp_title
            else:
                if k[0] == '':
                    texts_only[-1] = texts_only[-1] + k[1]
                    texts_with_title[-1][1] = texts_with_title[-1][1] + k[1]
                else:
                    temp = k[1]
                    temp_title = k[0]

                    if k[1][-1] == '。':
                        temp = clean_data(temp)
                        texts_with_title.append([temp_title,temp])
                        temp_list = split_to_sents(temp,(2,128))
                        for t in temp_list:
                            texts_only.append(t)
                        temp = ''
                        temp_title = ''       

                    else:
                        isStart = True

        return texts_only,texts_with_title    

def read_html(fileName):

    soup = BeautifulSoup(open(fileName,encoding='utf-8'),features='html.parser')
    res = []
    nums = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    marks = ['。','！','…','？','?','!','；',';','，']
    temp_label = ''   # 段落标签
    is_merge = False  # 针对pdf的分页

    for s in soup.strings:
        s = removeLineFeed(s)
        text = s.replace(' ','')
        if text != '':
            if text in nums:
                is_merge = True
                continue
            if len(text) < 2:
                continue                 
            if is_merge :
                is_merge = False
                if len(res) > 0:
                    res[-1][1] = res[-1][1] + clean_data(text) 
                temp_label = ''
                continue
            if text[0] in nums and text[1] == '.':
                start = 1
                for i in range(1,len(text)-1):
                    if text[i] in nums or text[i] == '.':
                        start = i  
                    else:
                        break
                temp_label = ''
                text = text[start+1:]   
            if text == '':
                continue
            isHasMark = False
            for mk in marks:
                if mk in text:
                    isHasMark = True
                    break
            if len(text) < 18 and not isHasMark:
                temp_label = text
            if '    ' in text:
                s = text.find('     ')
                temp_label = text[:s]
                text = text[s:]
            if len(text) > 18 or text[-1] == '。':
                temp_label = clean_data(temp_label)
                text = clean_data(text)
                res.append([temp_label,text])
                temp_label = ''

    texts_only = []
    texts_with_title = []
    isStart = True
    temp = ''
    temp_title = ''
    for k in res :
        if isStart :                  
            if k[0] != '':
                if k[1][-1] == '。':
                    temp = temp + k[1]
                    temp = clean_data(temp)
                    temp_title = temp_title + k[0]
                    texts_with_title.append([temp_title,temp])
                    temp_list = split_to_sents(temp,(2,128))
                    for t in temp_list:
                        texts_only.append(t)                       
                    temp = ''
                    temp_title = ''      
                    isStart = False
                else:
                    temp = temp + k[1]
                    temp_title = temp_title + k[0]
            if k[0] == '':
                if k[1][-1] == '。':
                    temp = temp + k[1]
                    temp = clean_data(temp)
                    temp_title = temp_title
                    texts_with_title.append([temp_title,temp])
                    temp_list = split_to_sents(temp,(2,128))
                    for t in temp_list:
                        texts_only.append(t)                
                    temp = ''
                    temp_title = ''      
                    isStart = False
                else:
                    temp = temp + k[1]
                    temp_title = temp_title
        else:
            if k[0] == '':
                texts_only[-1] = texts_only[-1] + k[1]
                texts_with_title[-1][1] = texts_with_title[-1][1] + k[1]
            else:
                temp = k[1]
                temp_title = k[0]
                if k[1][-1] == '。':
                    temp = clean_data(temp)
                    texts_with_title.append([temp_title,temp])
                    temp_list = split_to_sents(temp,(2,128))
                    for t in temp_list:
                        texts_only.append(t)
                    temp = ''
                    temp_title = ''       
                else:
                    isStart = True

    return texts_with_title

def read_xml(fileName):

    soup = BeautifulSoup(open(fileName,encoding='utf-8'),features='lxml')

    res = []
    nums = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    temp_label = ''   # 段落标签
    is_merge = False  # 针对pdf的分页

    for s in soup.strings:
        s = removeLineFeed(s)
        text = s.replace(' ','')

    for s in soup.strings:
        s = removeLineFeed(s)
        text = s.replace(' ','')
        if text != '':

            if text in nums:
                is_merge = True
                continue
            if len(text) < 2:
                continue                 
            if is_merge :
                is_merge = False
                if len(res) > 0:
                    res[-1][1] = res[-1][1] + clean_data(text) 
                temp_label = ''
                continue
            if text[0] in nums and text[1] == '.':
                start = 1
                for i in range(1,len(text)-1):
                    if text[i] in nums or text[i] == '.':
                        start = i  
                    else:
                        break
                temp_label = ''
                text = text[start+1:]   
            if text == '':
                continue
            if len(text) < 18 and not isHasMark(text):
                temp_label = text
            if '    ' in text:
                s = text.find('     ')
                temp_label = text[:s]
                text = text[s:]
            if len(text) > 18 or text[-1] == '。':
                temp_label = clean_data(temp_label)
                text = clean_data(text)
                if isHasMark(temp_label) or len(temp_label) > 25:
                    res.append(['', temp_label + text])
                else:
                    res.append([temp_label,text])
                temp_label = ''

    texts_only = []
    texts_with_title = []
    isStart = True
    temp = ''
    temp_title = ''

    for count,k in enumerate(res):    
        if isStart :                  
            if k[0] != '':
                if k[1][-1] == '。':
                    temp = temp + k[1]
                    temp = clean_data(temp)
                    temp_title = temp_title + k[0]
                    texts_with_title.append([temp_title,temp])
                    temp_list = split_to_sents(temp,(2,128))
                    for t in temp_list:
                        texts_only.append(t)                       
                    temp = ''
                    temp_title = ''      
                    isStart = False
    
                else:
                    temp = temp + k[1]
                    temp_title = temp_title + k[0]
    
            if k[0] == '':
                if k[1] != '':
                    if k[1][-1] == '。':
                        temp = temp + k[1]
                        temp = clean_data(temp)
                        temp_title = temp_title
                        texts_with_title.append([temp_title,temp])
                        temp_list = split_to_sents(temp,(2,128))
                        for t in temp_list:
                            texts_only.append(t)                
                        temp = ''
                        temp_title = ''      
                        isStart = False

                    else:
                        temp = temp + k[1]
                        temp_title = temp_title

        else:
            if k[0] == '':
                texts_only[-1] = texts_only[-1] + k[1]
                texts_with_title[-1][1] = texts_with_title[-1][1] + k[1]

            else:
                temp = k[1]
                temp_title = k[0]

                if count != len(res) - 1:
                    
                    # 2020/12/21 更新 增加判断 如果上一个标题以':'结束 且下一个标题并不为空则判断为不相关标题
                    if k[1][-1] == '。' or (k[1][-1] == '：' and res[count+1] != '') or  isHasPrefix:
                        temp = clean_data(temp)
                        texts_with_title.append([temp_title,temp])
                        temp_list = split_to_sents(temp,(2,128))
                        for t in temp_list:
                            texts_only.append(t)
                        temp = ''
                        temp_title = ''  
                    else:
                        isStart = True

                else :

                    if k[1][-1] == '。' :
                        temp = clean_data(temp)
                        texts_with_title.append([temp_title,temp])
                        temp_list = split_to_sents(temp,(2,128))
                        for t in temp_list:
                            texts_only.append(t)
                        temp = ''
                        temp_title = ''

                    else:
                        isStart = True
    return texts_with_title                   