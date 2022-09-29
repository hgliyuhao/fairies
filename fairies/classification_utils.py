from sklearn.model_selection import train_test_split
from collections import Counter
import random
import numpy as np


def split_classification_data(datas, test_size=0.1):
    """对多分类任务中，按照不同的方式划分数据集
    
    Parameters
    ----------
    datas = [
                {"id": 2214, "label": "2", "sentence": "我退货申请撤销 一下吧"},
                {"id": 1850, "label": "7", "sentence": "好的  谢谢，希望进完发货"}
    ]

    test_size  默认为0.1
    数据集每个类别划分为验证集的比例

    Returns
    ------- 
    和原始数据格式一样划分好的数据集train_data, test_data
    """

    data_dicts = {}

    train_data = []
    test_data = []

    for data in datas:

        label = data["label"]

        if label not in data_dicts:
            data_dicts[label] = []
        data_dicts[label].append(data)

    for label in data_dicts:

        num = len(data_dicts[label])
        if num == 0:
            continue

        test_num = int(num * test_size)
        random.shuffle(data_dicts[label])

        test_data.extend(data_dicts[label][:test_num])
        train_data.extend(data_dicts[label][test_num:])

    return train_data, test_data


def count_label(labels):

    result = Counter(labels)
    return (result)


def analysis_res(y_true, y_pred, label2name):
    """
        y_true = [0,0,1,2,1,0,2]
        y_pred = [0,1,1,1,1,2,2]
        label2name = {"0":体育,"1":"经济","2":"文化"}
        
    """

    # 转移矩阵

    true, pred = {}, {}
    transfer = {}

    for label in label2name:
        true[label] = 0
        pred[label] = 0
        transfer[label] = {}
        for new_label in label2name:
            transfer[label][label2name[new_label]] = 0
    for y in y_true:
        if y in true:
            true[y] += 1
    for i, p in enumerate(y_pred):
        if p == y_true[i]:
            pred[p] += 1
        transfer[y_true[i]][label2name[p]] += 1
    res, res_transfer = {}, {}
    for label in label2name:
        if true[label] == 0:
            res[label2name[label]] = [0, 0, 0]
        else:
            res[label2name[label]] = [
                pred[label], true[label], pred[label] / true[label]
            ]
        res_transfer[label2name[label]] = transfer[label]
    return res, res_transfer
