import json



def write_json(filename,res):
    json_str = json.dumps(res,ensure_ascii=False,indent=4)
    with open(filename, 'w',encoding = 'utf-8') as json_file:
                    json_file.write(json_str) 

def read_json(filename):
    try:
        with open(filename,'r',encoding='utf8') as f:
            json_data = json.load(f)
    except:
        json_data = []
        with open(filename,encoding='utf-8') as f:
            for line in f:
                json_data.append(json.loads(line))        
    return json_data

def write_text(fileName,lists,model = 'normal'):

    """
        按行写入
    """
    if model == 'normal':
        f = open(fileName,'w',encoding='utf8')
    else:    
        f = open(fileName, 'a',encoding='utf8')
    for i in lists:
        f.write(str(i))
        f.write('\n')
    f.close()

def reSort(filename,isReverse = True):
    
    """
        对字典或数组重新排序,
        isReverse 默认为true 默认越长的元素排在前面 为False 相反 
    """
    
    a = read_json(filename)
    a.sort(key=lambda a: len(a),reverse = isReverse)
    write_json(filename,a)

def get_file_size(fileName):
    # 获取文件大小
    return os.path.getsize(fileName)

def get_file_list(file_path):
    # 获取文件列表
    return os.listdir(file_path)        