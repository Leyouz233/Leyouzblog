title: 用Python使用Gmail发送邮件
date: 2021-06-16 13:38:32
introduce: 用Python使用Gmail发送邮件，遇到了很多奇奇怪怪的问题
tag: Python

### 前提
因为最近想要做一个自动发送邮件的邮件机器人FwRobot，又找不到好的服务器，所以就暂时使用PythonAnywhere，但是因为委委屈屈使用免费套餐，所以就只能访问白名单里面的网站，自然而然的网易邮箱的就不能使用了，就准备跳槽使用Google邮箱，不过嘞谷歌邮箱用起来也真是麻烦，所以在这里做了一下踩坑笔记

![源代码](/static/img/login-gmail/source-code.png)

#### 解读
其中的第27行，在`smtplib.SMTP`中加入`host='smtp.gmail.com'`貌似是必须的，不然会报错

然后第31、32、33也需要加进来

	smt_p.ehlo()
	smt_p.starttls()
	smt_p.ehlo()

### 其次
需要是需要在Google账号上面配置一下

### 大佬解决方案
然后是Stack Overflow上一位大佬的解决方案（我就是看这个学的，没错没错，这只是一篇摸鱼的文章）-> [链接](stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python/27515833#27515833)
