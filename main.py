# -*- coding: utf-8 -*- 

import web,json
import handleregister
from handle import Handle,SendMessage
from web.contrib.template import render_jinja

urls=(
	'/wx','Handle',
	'/wx/sendmessage','SendMessage',
	'/wx/register','Register',
    #'/MP_verify_RX39sdTWhT3TlHFl.txt','Auth'
)
app = web.application(urls,globals())

render = render_jinja(
	'templates',
	encoding = 'utf-8',
)

# #注册接口
class Register(object):
	def GET(self):
		try:
			data = web.input()
			code = data.code
			print (data, type(data), code)
			result = handleregister.query_openid2exist(code)
			return render.hello(openid = result.openID,code = result.code)
			# dj = json.dumps(data)
			# print(dj)
			# ddj = json.loads(dj)
			# code = ddj.get('code')
			# print (ddj,code,len(code))

		except Exception as e:
			print e
			return e
	def POST(self):
		try:
			data = web.data()
			print ('register post',data)
		except Exception as e:
			print e
			return e



if __name__ == "__main__":
	app.run()
