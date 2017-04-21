# -*- coding: utf-8 -*- 

import hashlib
import web
import reply
import receive

class Handle(object):
	def GET(self):
		try:
			data = web.input()
			if len(data) ==0:
				return "this is the handle view "
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = "hellozbf"
			
			list = [token,timestamp,nonce]
			list.sort()
			sha1 = hashlib.sha1()
			map(sha1.update,list)
			hashcode = sha1.hexdigest()
			print('handle/GET func:%s,%s'%(hashcode,signature))
			if hashcode == signature:
				return echostr
			else:
				return ""	
		except Exception,Argument:
			return Argument
	def POST(self):
		try:
			webData = web.data()
			#后台打印
			print('handle POST webdata',webData)
			recMsg = receive.parse_xml(webData)
			toUser = recMsg.FromUserName
			fromUser = recMsg.ToUserName
			print (recMsg.Event)
			if isinstance(recMsg,receive.Msg):
				if recMsg.MsgType =='text':
					content = u"测试中".encode('utf-8')
					replyMsg = reply.TextMsg(toUser,fromUser,content)
				if recMsg.MsgType == 'image':
					mediaId = recMsg.MediaId
					replyMsg = reply.ImageMsg(toUser,fromUser,content)
				return replyMsg.send()
			if isinstance(recMsg,receive.EventMsg):
				if recMsg.Event == 'CLICK':
					if recMsg.Eventkey == 'zbf':
						content = u"编写中".encode('utf-8')
						replyMsg = reply.TextMsg(toUser,fromUser,content)
						return replyMsg.send()
			else:
				print('not handle now')
				return reply.Msg().send()
		except Exception,e:
			return e

