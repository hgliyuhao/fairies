import time
import os
import time
import logging
import sys
from functools import wraps
import traceback

def clock(func):
    """ 计算时间装饰器 """
    def clocked(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, int(end - start))
        return  result
    return clocked
