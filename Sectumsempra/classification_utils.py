from sklearn.model_selection import train_test_split
from collections import Counter

def random_split_data(all_data,label_name,test_size = 0.25,seed = 0):

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
    print(result)

    return(result)