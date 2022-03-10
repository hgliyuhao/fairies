from sklearn.model_selection import train_test_split
from collections import Counter
import random
import numpy as np

def split_data(
    all_data,
    model = "smoothing_ratios",
    test_size = 0.2
):
    
    """对多分类任务中，按照不同的方式划分数据集
    
    Parameters
    ----------
    all_data : 原始数据集
        需要确定数据集的格式,需要保证每条数据中包含"id","label"
        datasets = [
            {"id": 2214, "label": "2", "sentence": "我退货申请撤销 一下吧"},
            {"id": 1850, "label": "7", "sentence": "好的  谢谢，希望进完发货"}
        ]
    model : 默认为smoothing_ratios
        if model == "same_ratios"
            按照数据集中每个类别的比例进行训练集的划分
        if model = "smoothing_ratios"
            对数据集中每个类别的比例平滑后进行训练集的划分
    test_size  默认为0.2
        数据集每个类别划分为验证集的比例
        
    Returns
    ------- 
    和all_data格式一样的经过增强后的数据集
    """

    labels = set()  #标签集合
    label_count = {} #标签数量计算
    label_lists = {}
    all_data_count = len(all_data)

    for data in all_data:
        label = data["label"]
        labels.add(label)
        if label not in label_count:
            label_count[label] = 0
        if label not in label_lists:
            label_lists[label] = []

        label_count[label] += 1
        label_lists[label].append(data["id"])

    labels = list(set(labels))
    labels.sort()

    train_id, dev_id = [],[]
    train_data,dev_data = [],[] 
    
    if model == "same_ratios":
        for label in label_count:
        # 如果为0则不放入
            need_size = int(test_size * label_count[label])
            indexs = random.sample(range(label_count[label]), need_size)
            dev_id.extend(list(np.asarray(label_lists[label])[indexs]))

    elif model == "smoothing_ratios":
        label_count = sorted(label_count.items(),  key=lambda d: d[1], reverse=False)
        isLegal = False
        import collections
        label_count = collections.OrderedDict(label_count)
        for label in label_count:
            if label_count[label] >= 10:
                isLegal = True
                base = label_count[label]
                break

        if not isLegal:
            raise ValueError(
                "You Need More Data!"
            )  

        for label in label_count:
        # 如果为0则不放入

            if label_count[label] < base:
                need_size = int(test_size * label_count[label])
                indexs = random.sample(range(label_count[label]), need_size)
                dev_id.extend(list(np.asarray(label_lists[label])[indexs]))
            else:
                need_size = int(test_size * (label_count[label] **0.5) * (base **0.5))
                indexs = random.sample(range(label_count[label]), need_size)
                dev_id.extend(list(np.asarray(label_lists[label])[indexs]))
                print(need_size)
    for data in all_data:
        id = data["id"]
        if id in dev_id:
            dev_data.append(data)
        else:
            train_data.append(data)    

    return train_data,dev_data

def random_split_data(all_data,label_name,test_size = 0.20,seed = 0):

    labels = []
    for line in all_data:
        labels.append(int(line[label_name]))
    train_idx, test_idx, _, _ = train_test_split(range(len(labels)), labels, stratify=labels,
                                                    shuffle=True, test_size=test_size, random_state=seed)
    
    train_data,test_data = [],[]

    for i in train_idx:
        train_data.append(all_data[i])

    for i in test_idx:
        test_data.append(all_data[i])

    return train_data,test_data    

def count_label(labels):

    result = Counter(labels)
    return(result)

def analysis_res(y_true, y_pred,lable2name):
    
    """
        y_true = [0,0,1,2,1,0,2]
        y_pred = [0,1,1,1,1,2,2]
        lable2name = {"0":体育,"1":"经济","2":"文化"}

        {   
            '体育': [1, 3, 0.33], 
            '经济': [2, 2, 1.0], 
            '文化': [1, 2, 0.5]}
        }    
    """
    true,pred = {},{}
    for lable in lable2name:
        true[lable] = 0
        pred[lable] = 0
    for y in y_true:
        if y in true:
            true[y] += 1
    for i,p in enumerate(y_pred):
        if p == y_true[i]:
            pred[p] += 1
    res = {}
    for lable in lable2name:
        if true[lable] == 0:
            res[lable2name[lable]] = [0,0,0]
        else:    
            res[lable2name[lable]] = [pred[lable],true[lable],pred[lable]/true[lable]]

    return res    


