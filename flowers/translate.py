import http.client
import hashlib
import urllib
import random
import json
import time
import file_utils

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