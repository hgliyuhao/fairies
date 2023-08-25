import random
from collections import defaultdict


def split_classification_data(datas,
                              label_key="label",
                              test_size=0.1,
                              random_seed=None):
    """对多分类任务中，按照不同的方式划分数据集
    
    Parameters
    ----------
    datas: List[Dict]
        例如: [{"id": 2214, "label": "2", "sentence": "我退货申请撤销 一下吧"}, ...]
    
    label_key: str, default "label"
        字典中用作类标签的键。

    test_size: float, default 0.1
        数据集每个类别划分为验证集的比例。

    random_seed: int, optional
        随机种子。

    Returns
    ------- 
    和原始数据格式一样划分好的数据集 train_data, test_data
    """

    if random_seed:
        random.seed(random_seed)

    data_dicts = defaultdict(list)
    train_data = []
    test_data = []

    for data in datas:
        label = data[label_key]
        data_dicts[label].append(data)

    for label_data in data_dicts.values():
        random.shuffle(label_data)

        test_num = int(len(label_data) * test_size)
        test_data.extend(label_data[:test_num])
        train_data.extend(label_data[test_num:])

    return train_data, test_data
