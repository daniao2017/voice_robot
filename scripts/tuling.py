#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
#import urllib2
import json
import requests
import rospy
import time
from std_msgs.msg import String
reload(sys)
sys.setdefaultencoding('utf-8')
flag = 0
test = 0
results_text ='777'
url = "http://openapi.tuling123.com/openapi/api/v2"


def jiegou():
    req = {
    "perception":
    {
        "inputText":
        {
            "text": data_input
        },

    },
    "userInfo":
    {
        "apiKey": "7b20d5b3648544948ab5767732a51f34",
        "userId": "123"
    }}
    global data_json
    data_json = json.dumps(req).encode('utf8')

def tuling_callback(data):
    #rospy.loginfo("your questions is %s",data.data) 
    global  data_input
    data_input = str(data.data)
    jiegou()
    #print("测试")
    test_result()
    #time.sleep(2)
    global flag 
    flag = 1


def test_result():

    a = requests.post(url,data_json)  # 使用post请求
    content = (a._content).decode('utf-8')  # 获取返回结果_content属性，解码
    res = json.loads(content)  # 反序列化
    intent_code = res['intent']['code']
    global results_text
    results_text = res['results'][0]['values']['text']
    
    #print(str(intent_code))
    print(results_text)
    #global flag 
    #flag = 1 

def tuling_talker():
    while(1):
        rospy.init_node("tuling_node_py")
        pub = rospy.Publisher("/voice/xf_tts_topic",String,queue_size=10)
        rospy.Subscriber("voice/tuling_nlu_topic",String,tuling_callback)
        rate = rospy.Rate(1000)
        global flag
        while not rospy.is_shutdown():
            if(flag):
                hello_str = str(results_text)
                pub.publish(hello_str)
                flag=0
                rate.sleep()

if __name__ == '__main__':
    try:
        tuling_talker()
    except rospy.ROSInterruptException:
        pass
