#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import json
import requests
import rospy
from std_msgs.msg import String
import sys
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
    global  data_input
    data_input = str(data.data)
    jiegou()
    test_result()


def test_result():

    a = requests.post(url,data_json)  # 使用post请求
    content = (a._content).decode('utf-8')  # 获取返回结果_content属性，解码
    res = json.loads(content)  # 反序列化
    intent_code = res['intent']['code']
    results_text = res['results'][0]['values']['text']
    print(results_text)
    #pub_tts.publish(results_text)
    pub_hwtts.publish(results_text)


if __name__ == '__main__':
    rospy.init_node("tuling_node_py")
    pub_hwtts = rospy.Publisher("/voice/hw_tts_topic",String,queue_size=1)
    pub_tts = rospy.Publisher("/voice/xf_tts_topic",String,queue_size=1)
    rospy.Subscriber("voice/tuling_nlu_topic",String,tuling_callback)
    rospy.spin()
