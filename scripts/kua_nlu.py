#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import rospy
from std_msgs.msg import String

def nlu_cb(data):
    name = data.data
    with open("/home/danoao/代码/vscode 学习/python/nlu/彩虹屁语句.txt","r")as f:
        lines= f.readlines()
    lines=[line.strip() for line in lines]
    random.shuffle(lines)
    template ="""{},今天我不得不夸夸你。
    你知道吗？{}
    也许你不相信，但{}
    你不要不好意思，真的，{}
    我知道你会否认，不过{}
    也许你不知道，{}
    可我们都知道，{}
    总之，{}
    这就是我今天想对你说的全部！"""
    compliment=template.format(name,*lines)
    #pub_hwtts.publish(compliment)
    pub_xftts.publish(compliment)

if __name__ == "__main__":
    rospy.init_node('kua_nlu', anonymous=True)
    rospy.Subscriber("/voice/kua_nlu_topic", String, nlu_cb)
    pub_xftts =rospy.Publisher("/voice/xf_tts_topic", String,queue_size=10)
    pub_hwtts =rospy.Publisher("/voice/hw_tts_topic", String,queue_size=10)
    rospy.spin()