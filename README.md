# voice_robot
💖小刘同学是一款语音交互的机器人，作者小刘同学。
演示视频如下：[小刘同学二代的全部功能演示](https://www.bilibili.com/video/BV1n54y1D7Bc)
功能如下:

基本的语言交互机器人

 - awake移植了snowboy
 - asr移植的是讯飞asr的c语言sdk
 - nlu是api调用图灵机器人
 - tts有讯飞与华为两种方式
 
通信层

 **暂时使用的是ros，后期准备提取通信层到stm32**
 
 
 插件中心
 
 用来控制各种资源的调度情况，特别是asr与tts的情况
 
 现有如下功能插件
 
 - 百度翻译，支持汉译英
 - 网易云音乐，爬取网易云音乐
 - 发送邮件，发送邮件

 
