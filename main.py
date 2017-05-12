# -*- coding: utf-8 -*- 

import web,json
import handleregister
from handle import Handle,SendMessage,GetSNSToBind
from web.contrib.template import render_jinja
from messagemodle import ResultModle
from handleregister import Result

urls=(
	'/wx','Handle',
	'/wx/sendmessage','SendMessage',
	'/wx/register','Register',
	'/wx/getsns2bind','GetSNSToBind'
)
app = web.application(urls,globals())

render = render_jinja(
	'templates',
	encoding = 'utf-8',
)

#注册接口
class Register(object):
	#校验openid的有效性
	def GET(self):
		try:
			data = web.input()
			code = data.code
			print (data, type(data), code)
			openid = handleregister.getopenid(code)
			result = handleregister.query_openid2exist(openid)
			print(result.code,result.openID)
			return render.register(openid = result.openID,code = result.code)
		except Exception as e:
			print e
			return e

	#绑定账号
	def POST(self):
		result = ResultModle()
		try:
			data = web.data()
			ddata = json.loads(data)
			print ('register post', data)
			send = Result()
			send.tellNumber = ddata.get('tel')
			send.code = ddata.get('sns')
			send.openID = ddata.get('openid')
			sresult = handleregister.check_sms(send)
			if sresult == None:
				result.errmsg = u'绑定成功'
				result.errorcode = 30030
				dresult = result.__dict__
				jresult = json.dumps(dresult)
				print ('zbf in register',jresult)
				web.header("Access-Control-Allow-Origin", "*")
				return jresult
		except Exception as e:
			print e
			result.errmsg = u'绑定失败'
			result.errorcode = 30031

			dresult = result.__dict__
			jresult = json.dumps(dresult)
			print ('zbf in register', jresult)
			web.header("Access-Control-Allow-Origin", "*")
			return jresult



if __name__ == "__main__":
	app.run()
