# -*- coding: utf-8 -*- 

import web,json
import handleregister
from handle import Handle,SendMessage,GetSNSToBind
from web.contrib.template import render_jinja

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
			return render.hello(openid = result.openID,code = result.code)
		except Exception as e:
			print e
			return e

	#绑定账号
	def POST(self):
		try:
			data = web.data()

			print ('register post',data)
		except Exception as e:
			print e
			return e



if __name__ == "__main__":
	app.run()
