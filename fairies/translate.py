import http.client
import hashlib
import urllib
import random
import json
import time
from fairies import file_utils

def zh_to_en(word_lists):

    """
        只会返回前200的单词翻译
        使用百度api
    """

    appid = '20201107000610595'  # 填写你的appid
    secretKey = 'EylFfm6wOcWQRNaI3LZ9'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    final_res = []
    count = 0
    for i in word_lists[:200]:
        count += 1

        if count % 50 == 0:
            time.sleep(30)        
        else:    
            time.sleep(1)
        try:

            fromLang = 'zh'   #原文语种
            toLang = 'en'   #译文语种
            salt = random.randint(32768, 65536)
            q = i
            sign = appid + q + str(salt) + secretKey
            sign = hashlib.md5(sign.encode()).hexdigest()
            myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            print('正在请求...')
            print(result)
            re = result['trans_result'][0]['dst']
            final_res.append(re)

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()
    
    return final_res

def en_to_zh(word_lists):

    """
        只会返回前200的单词翻译
        使用百度api
    """

    appid = '20201107000610595'  # 填写你的appid
    secretKey = 'EylFfm6wOcWQRNaI3LZ9'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'


    final_res = []
    count = 0
    for i in word_lists[:200]:
        count += 1

        if count % 50 == 0:
            time.sleep(30)        
        else:    
            time.sleep(1)
        try:

            fromLang = 'en'   #原文语种
            toLang = 'zh'   #译文语种
            salt = random.randint(32768, 65536)
            q = i
            sign = appid + q + str(salt) + secretKey
            sign = hashlib.md5(sign.encode()).hexdigest()
            myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            print('正在请求...')
            print(result)
            re = result['trans_result'][0]['dst']
            final_res.append(re)

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()
    
    return final_res

def translate(from_type,to_type,word_lists):

    """
        支持任何语言种类间的转换

        # 自动检测 auto
        # 中文 zh
        # 英语 en
        # 粤语 yue
        # 文言文 wyw
        # 日语 jp
        # 韩语 kor
        # 法语 fra
        # 西班牙语 spa
        # 泰语 th
        # 阿拉伯语 ara
        # 俄语 ru
        # 葡萄牙语 pt
        # 德语 de
        # 意大利语 it
        # 希腊语 el
        # 荷兰语 nl
        # 波兰语 pl
        # 保加利亚语 bul
        # 爱沙尼亚语 est
        # 丹麦语 dan
        # 芬兰语 fin
        # 捷克语 cs
        # 罗马尼亚语 rom
        # 斯洛文尼亚语 slo
        # 瑞典语 swe
        # 匈牙利语 hu
        # 繁体中文 cht
        # 越南语 vie
        
    """

    appid = '20201107000610595'  # 填写你的appid
    secretKey = 'EylFfm6wOcWQRNaI3LZ9'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    final_res = []
    count = 0
    for i in word_lists[:200]:
        count += 1

        if count % 50 == 0:
            time.sleep(30)        
        else:    
            time.sleep(1)
        try:

            fromLang = from_type   #原文语种
            toLang = to_type   #译文语种
            salt = random.randint(32768, 65536)
            q = i
            sign = appid + q + str(salt) + secretKey
            sign = hashlib.md5(sign.encode()).hexdigest()
            myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            print('正在请求...')
            print(result)
            re = result['trans_result'][0]['dst']
            final_res.append(re)

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()
    
    return final_res        