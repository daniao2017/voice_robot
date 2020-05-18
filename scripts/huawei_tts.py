#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import base64
import json
import requests
from HttpRequest import HttpRequests
import sys
reload(sys)
import time
sys.setdefaultencoding( "utf-8" )
import rospy 
from std_msgs.msg import String
import os
headers = {"content-type": "application/json"}
url = "https://sis-ext.cn-north-4.myhuaweicloud.com/v1/0629bb1a768026c42fffc00e25759f39/tts"
def get_token():
    try:
        f = open("/home/danoao/文档/test.txt", 'r')
        token_str = f.read().encode('utf-8')
        f.close()
        token_info = json.loads(token_str)
        global headers
        headers["x-auth-token"] = token_info["token"]
        print('读取token成功')
        
    except:
        print('读取失败')




def get_tts(content):
    tts_data ={
        "text": content,
    "config": { 
     "audio_format": "wav", 
     "sample_rate": "8000", 
     "property": "chinese_xiaoyan_common",
     "speed": 10,
     "pitch": 10,
     "volume": 60}
    }

    call_req = HttpRequests(url, data=json.dumps(tts_data),type="POST", headers =headers)
    if(call_req.get_code()==200):
       a = call_req.get_text()
       b= json.loads(a)
       print("连接资源成功")
       data = b["result"]["data"]
       #print(str(data))
    
       f = open('/home/danoao/文档/tts.wav','wb')
       two_data=  base64.b64decode(str(data))
       f.write(two_data)
       f.close()
       os.system("play /home/danoao/文档/tts.wav ")
       #print(two_data)
    else:
        print(call_req.get_code())
        print("连接失败")
def tts_cb(data):
  content = data.data
  get_token()
  get_tts(content)




if __name__ == "__main__":
  rospy.init_node('huawei_tts_node', anonymous=True)
  rospy.Subscriber("/voice/hw_tts_topic", String, tts_cb)
  rospy.spin()
