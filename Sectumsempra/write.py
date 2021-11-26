import json
import codecs
from tqdm import tqdm

def write_json(filename,res,isIndent = True):
    
    if isIndent:
        json_str = json.dumps(res,ensure_ascii=False,indent=4)
        with open(filename, 'w',encoding = 'utf-8') as json_file:
            json_file.write(json_str)
    else:        
        with codecs.open(filename, 'w', 'utf-8') as f:
            for formatted_instance in res:
                json_str = json.dumps(formatted_instance, ensure_ascii=False)
                f.write(json_str)
                f.write('\n')
        f.close()

def write_txt(fileName,lists,model = 'normal'):

    """
        按行写入
    """

    if model == 'normal':
        f = open(fileName,'w', encoding='utf8')
    else:    
        f = open(fileName, 'a', encoding='utf8')
    for i in tqdm(lists):
        f.write(str(i))
        f.write('\n')
    f.close()