#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import httplib
import md5
import urllib
import rospy
from std_msgs.msg import String

appid = '20200321000402432' #你的appid
secretKey = 'JAsYtWTeABObB3c5iv_V' #你的密钥

httpClient = None
def noise():
    myurl = '/api/trans/vip/translate'
    fromLang = 'zh'
    toLang = 'en'
    salt = "123456"
    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    global baidu_url
    baidu_url = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
def callback(data):
    data = data.data
    global q 
    q = data
    noise()
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', baidu_url)
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        a = response.read()
        b= json.loads(a)
        #c = b["trans_result"]
        # print(c)
        src = b["trans_result"][0]["src"]
        print("中文：")
        print(src)
        dst = b["trans_result"][0]["dst"]
        print("英文：")
        print(dst)
        baidu_pub.publish(dst)
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
def baidu_translate():
    rospy.init_node('baidu_translate_node', anonymous=True)
    rospy.Subscriber("/voice/baidu_tl_topic", String, callback)
    global baidu_pub
    baidu_pub =rospy.Publisher("/voice/xf_tts_topic",String, queue_size=3)
    rospy.spin()

if __name__ == "__main__":
    baidu_translate()
    
