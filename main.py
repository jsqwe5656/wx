# -*- coding: utf-8 -*- 

import web
from handle import Handle,SendMessage
from web.contrib.template import render_jinja

urls=(
	'/wx','Handle',
	'/wx/sendmessage','SendMessage',
	'/wx/register','Register'
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
			data = web.data()
			openid = data.openid
			return render.hello(name='zbf')
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
