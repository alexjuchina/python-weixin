#coding:utf-8
import itchat
import requests
import re
def login_sendmsg(text):
	#itchat.login()  # 只是普通的登陆，并不具有缓存的功能
	itchat.auto_login(hotReload=True)   # 可以暂存登陆状态
	friend = itchat.search_friends(u'ALEX')[0]#XX为好友的备注或名称
	itchat.send_msg(text, friend["UserName"])#text是要发送的内容
	#itchat.send_file()发送文件
	#itchat.send_image发送图片
	#itchat.send_video 发送视频...
if __name__ == '__main__':
	text = ["test1","test2"]
	login_sendmsg(text[0])
	login_sendmsg(text[1])
