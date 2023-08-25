import re

def removeLineFeed(text):
    """去除换行和tab键"""
    return re.sub(r'[\r\n\t]', ' ', text)

def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    return any(u'\u4e00' <= ch <= u'\u9fff' for ch in string)

def find_lcs(s1, s2):
    """Find the longest common substring between s1 and s2."""
    m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_len, p = 0, 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > max_len:
                    max_len = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - max_len:p], max_len