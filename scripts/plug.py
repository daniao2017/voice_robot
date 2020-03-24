#!/usr/bin/python
# -*- coding: UTF-8 -*-

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
#from  voice_system.msg import voice_test
flag = 0
email_flag = 0
nlu_flag = 0
baidu_flag = 0
wangyi_flag =0 

def plug_callback(data):
    result  = data.data
    global flag
    flag = 0
    if(result == "发送邮件。"):
        flag = 1
        global email_flag 
        email_flag = 1
        print("邮件唤醒成功")
        pub_asr.publish(flag)
        print("请说出你要发送的邮件内容")
    elif (result=="图灵机器人。") :
        flag = 1
        global nlu_flag
        nlu_flag = 1
        print("nlu语音交互功能启动")
        pub_asr.publish(flag)
        print("请开始你的问题把")
    elif (result=="百度翻译。") :
        flag = 1
        global baidu_flag
        baidu_flag = 1
        print("百度翻译功能启动")
        pub_asr.publish(flag)
        print("请输入你想翻译的内容")

    elif (result=="网易音乐。") :
        flag = 1
        global wangyi_flag
        wangyi_flag = 1
        print("爬虫启动")
        pub_asr.publish(flag)
        print("请输入你想听的歌手名")

    else:
        pass
    if(flag==0 and email_flag == 1) :
        print("开始发送邮件")
        pub_email.publish(result)
        print(result)
        email_flag = 0
    if(flag ==0 and nlu_flag==1):
        pub_nlu.publish(result)
        print("你的问题是：")
        print(result)
        nlu_flag =0
    if(flag ==0 and baidu_flag==1):
        print("################")
        pub_baidu.publish(result)
        
        baidu_flag =0
    if(flag ==0 and wangyi_flag==1):
        print("################")
        pub_wangyi.publish(result)
        wangyi_flag =0





def plug():
    rospy.init_node('plug_node', anonymous=True)
    rospy.Subscriber("/voice/plug",String, plug_callback)
    #print("测试")
    global pub_asr
    global pub_email
    global pub_nlu
    global pub_baidu
    global pub_wangyi
    pub_asr = rospy.Publisher("/voice/xf_asr_topic",Int32,queue_size=1)
    pub_email=rospy.Publisher("/voice/email_topic", String,queue_size=1)
    pub_nlu=rospy.Publisher("/voice/tuling_nlu_topic", String,queue_size=1)
    pub_baidu = rospy.Publisher('/voice/baidu_tl_topic', String, queue_size=1)
    pub_wangyi = rospy.Publisher("/voice/wangyi_topic",String,queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    plug()
