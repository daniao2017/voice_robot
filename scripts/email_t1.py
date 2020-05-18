#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import smtplib
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart 

import smtplib
import rospy
from std_msgs.msg import String

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="2868108923@qq.com"    #用户名
mail_pass="boxxhhbgvtcldgej"   #口令 
sender = '2868108923@qq.com' 
receivers = ['2868108923@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
subject = '【百度证书】7日深度学习打卡第六期'
message = MIMEMultipart() 

def add_text_yourname(yourname):

    test1 = str(yourname)
    test1.replace("。","")
    #设置所使用的字体
    font = ImageFont.truetype("/home/danoao/catkin_ws/src/voice_system/source/simhei.ttf", 80)
    #打开图片
    imageFile = "/home/danoao/catkin_ws/src/voice_system/source/刘高杰.jpg"
    #opencv
    im3 = cv2.imread(imageFile)
    #测试使用
    im4 = im3[900:1200,600:1000]
    img_black = np.zeros((300,400,3), np.uint8)
    img_black.fill(255)
    im3[900:1200,600:1000] = img_black
    #还原真实底片
    tmp_img = "/home/danoao/catkin_ws/src/voice_system/source/test.jpg"
    cv2.imwrite(tmp_img,im3)
    your_img = cv2.imread(tmp_img)
    #将numpy array的图片格式转为PIL的图片格式
    img_pil = Image.fromarray(your_img)
    draw = ImageDraw.Draw(img_pil)
    #写文字
    draw.text(xy=(600, 1100), text = test1, font = font, fill = (0, 0, 0))
    bk_img = np.array(img_pil)  
    #打开图片
    f_img = bk_img
    bk_img = bk_img[:,:,[2,1,0]]
    cv2.imwrite("/home/danoao/catkin_ws/src/voice_system/source/show.jpg",f_img)

def email_callback(data):
    sounds = data.data
    yourname = sounds
    add_text_yourname(yourname)
    
    #message = MIMEText(message_fix, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("Ding,Jin", 'utf-8') #发件人
    message['To'] =  Header("高杰邮箱", 'utf-8')
    html_file = "/home/danoao/代码/vscode 学习/html/test.html"
    sendFile = open(html_file,"rb").read()
    message.attach(MIMEText(open(html_file,"rb").read(), 'html', 'utf-8'))
    # 构造附件
    att_file = "/home/danoao/catkin_ws/src/voice_system/source/show.jpg"
    sendFile = open(att_file,"rb").read()
    att2 = MIMEText(sendFile, 'base64', 'utf-8') 
    att2['Content-Type'] = 'application/octet-stream' 
    att2['Content-Disposition'] = 'attachment; filename="reward.jpg"' 
    message.attach(att2)
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
if __name__ == "__main__":
    rospy.init_node('email_listener', anonymous=True)
    rospy.Subscriber("/voice/email_topic", String, email_callback)
    rospy.spin()