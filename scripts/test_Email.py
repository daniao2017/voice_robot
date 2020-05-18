#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from email.mime.text import MIMEText
from email.header import Header

email_flag = 1 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="2868108923@qq.com"    #用户名
mail_pass="boxxhhbgvtcldgej"   #口令 
sender = '2868108923@qq.com' 
receivers = ['2868108923@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
subject = 'ROS机器人发送邮件'
#global message
#message = MIMEText(sounds, 'plain', 'utf-8')
#message['Subject'] = Header(subject, 'utf-8')

#message['From'] = Header("ROS机器人", 'utf-8')
#message['To'] =  Header("高杰邮箱", 'utf-8') 

 
 
def email_callback(data):
    sounds = data.data
    global email_flag
    email_test = 1

    message = MIMEText(sounds, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("ROS机器人", 'utf-8')
    message['To'] =  Header("高杰邮箱", 'utf-8') 
    if(sounds =="发送邮件。"):
        email_flag = 1
        print("邮件功能唤醒成功")
        pub.publish(email_flag)
        email_flag =0
        email_test = 0 
        print("请说出你要发送的邮件内容")
    if (email_flag ==0 and email_test==1): 
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print "邮件发送成功"
        except smtplib.SMTPException:
            print "Error: 无法发送邮件"

def email_listener():
    rospy.init_node('email_listener', anonymous=True)
    rospy.Subscriber("/voice/email_topic", String, email_callback)
    global pub
    pub = rospy.Publisher("/voice/xf_asr_topic",Int32,queue_size=1)
    rospy.spin()

if __name__ == "__main__":
    email_listener()