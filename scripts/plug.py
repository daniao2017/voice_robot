#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
#from  voice_system.msg import voice_test
flag = 0
email_flag = 0
nlu_flag = 0
baidu_flag = 0
wangyi_flag =0 
huawei_flag = 0
kua_flag = 0

def plug_callback(data):
    result  = data.data
    global flag
    flag = 0
    if(result == "发送邮件。"):
        flag = 1
        global email_flag 
        email_flag = 1
        print("邮件唤醒成功")
        pub_xftts.publish("邮件唤醒成功")
        time.sleep(3)
        pub_xftts.publish("请说出你要发送的邮件内容")
        time.sleep(3)
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
        wangyi_flag = 1
        pub_asr.publish(flag)
        print("请输入你想听的歌手名")
    elif (result =="华为TTS。"):
        global huawei_flag 
        wangyi_flag = 1
        print("华为tts功能启动")
    elif (result =="夸夸人。"):
        flag = 1
        global kua_flag
        kua_flag = 1
        print ("夸夸人功能启动")
        pub_asr.publish(flag)
        print("请说出你要夸夸人的名字") 
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
    if(flag==0 and huawei_flag == 1) :
        print("################")
        pub_hwtts.publish("tts")
        huawei_flag = 0 
    if (flag == 0 and kua_flag ==1):
        print("#####################")
        pub_kuakua.publish(result)
        kua_flag = 0







if __name__ == '__main__':
    rospy.init_node('plug_node', anonymous=True)
    rospy.Subscriber("/voice/plug",String, plug_callback)
    #华为tts
    pub_hwtts =rospy.Publisher("/voice/hw_tts_topic", String,queue_size=10) 
    #科大讯飞tts
    pub_xftts =rospy.Publisher("/voice/xf_tts_topic", String,queue_size=10)
    #科大讯飞一句话识别
    pub_asr = rospy.Publisher("/voice/xf_asr_topic",Int32,queue_size=1)
    #发送邮件
    pub_email=rospy.Publisher("/voice/email_topic", String,queue_size=10)
    #图灵机器人
    pub_nlu=rospy.Publisher("/voice/tuling_nlu_topic", String,queue_size=10)
    #百度翻译
    pub_baidu = rospy.Publisher('/voice/baidu_tl_topic', String, queue_size=1)
    #网易音乐
    pub_wangyi = rospy.Publisher("/voice/wangyi_topic",String,queue_size=1)
    #跨垮机器人
    pub_kuakua = rospy.Publisher("/voice/kua_nlu_topic",String,queue_size=1)
    rospy.spin()

