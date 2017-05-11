# -*- coding: utf-8 -*- 

import hashlib
import web,json
import reply
import receive
import modlemessage,handleregister

from messagemodle import ResultModle,HealthMessage,BOData,BPMdata,MessageValue,MessageModle

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
			if isinstance(recMsg,receive.Msg):
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				if recMsg.MsgType =='text':
					content = u"客服暂未开放，如需帮助请点击菜单旗舰店联系客服，或者拨打售后服务热线400-820-6276".encode('utf-8')
					replyMsg = reply.TextMsg(toUser,fromUser,content)
				if recMsg.MsgType == 'image':
					mediaId = recMsg.MediaId
					replyMsg = reply.ImageMsg(toUser,fromUser,content)
				return replyMsg.send()
			if isinstance(recMsg,receive.EventMsg):
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				print (recMsg.Event,recMsg.EventKey)
				if recMsg.Event == 'CLICK':
					if recMsg.EventKey == 'zbf':
						content = u"编写中".encode('utf-8')
						replyMsg = reply.TextMsg(toUser,fromUser,content)
						return replyMsg.send()
			else:
				print('not handle now')
				return reply.Msg().send()
		except Exception,e:
			return e

#发送健康数据
def sendHealthMessage(openID,mode,data):
	value = MessageValue()
	if mode ==0:
		value.first = {"value": "血氧测量提醒", "color": "#173177"}
		value.keyword1 = {"value": data.time, "color": "#173177"}
		value.keyword2 = {"value": "血氧饱和度", "color": "#173177"}
		str = u"血氧饱和度:"+ data.spo2 + u" 心率:" + data.bmp + u" 血流灌注指数:" + data.pi
		value.keyword3 = {"value":str , "color": "#173177"}
		value.keyword4 = {"value": data.message, "color": "#173177"}
		value.remark = {"value": "感谢您的使用", "color": "#173177"}
	else:
		value.first = {"value": "血压测量提醒", "color": "#173177"}
		value.keyword1 = {"value": data.time, "color": "#173177"}
		value.keyword2 = {"value": "23333", "color": "#173177"}
		value.keyword3 = {"value": "12138", "color": "#173177"}
		value.keyword4 = {"value": data.message, "color": "#173177"}
		value.remark = {"value": "感谢您的使用", "color": "#173177"}
	dvalue = value.__dict__
	values = MessageModle()
	values.template_id = "LZ3DwtGM8rU13Z_lWInZEvW2rRai3HHEdyMnWIR6YwE"
	values.touser = openID
	values.data = dvalue
	dvalues = values.__dict__
	jvalues = json.dumps(dvalues)
	print(jvalues)
	return modlemessage.send_message(jvalues)

#处理json
def checkHealthMessage(param):
	healthdata = HealthMessage()
	healthdata.__dict__ = json.loads(param)
	print(healthdata.__dict__)
	mode = healthdata.messageMode
	if  mode == 0:		#血氧
		data_bo=BOData()
		data_bo.__dict__ = healthdata.data
		return sendHealthMessage(healthdata.openID,mode,data_bo)
	elif mode == 1:		#血压
		data_bpm = BPMdata()
		data_bpm.__dict__ = healthdata.data
		return sendHealthMessage(healthdata.openID, mode, data_bpm)

#推送消息接口
class SendMessage(object):
	#占位的get
	def GET(self):
		try:
			data = web.input()
			print(data)
			if len(data) == 0:
				return "this is the handle view2 "
			else:
				openid = data.openid
				return openid
		except Exception as e:
			print (e)
			return e

	#{"phoneNumber":123,"openID":"oKtGus_DR1lrf0zhdQuec-PKtIOM","messageMode":0,"data":{"message":"message","time":"123132","spo2":"98%","bmp":"82bmp","pi":"9.1%"}}
	#推送公众号模板消息接口
	def POST(self):
		result = ResultModle()
		try:
			webdata = web.data()
			print(webdata)
			return checkHealthMessage(web.data())
		except Exception as e:
			result.errorcode = 30050
			result.errmsg = e.message
			dresult = result.__dict__
			jresult = json.dumps(dresult)
			return jresult

#请求短信验证码
class GetSNSToBind(object):

	#请求短信验证码
	def POST(self):
		result = ResultModle()
		try:
			data = web.data()
			print ('GetSNSToBind post', data)
			ddata = json.loads(data)
			tel = ddata.get('tel')
			result = handleregister.query_tel2openid(tel)
			print ('zbfasd',result)
			# web.header("content-type","application/json")
			web.header("Access-Control-Allow-Origin","*")
			# web.header("Access-Control-Allow-Methods","POST")
			# web.header("Access-Control-Allow-Headers","x-requested-with/content-type")
			return result
		except Exception as e:
			print e
			result.errorcode = 30050
			result.errmsg = u'发送失败'
			dresult = result.__dict__
			jresult = json.dumps(dresult)
			web.header("Access-Control-Allow-Origin", "*")
			return jresult


