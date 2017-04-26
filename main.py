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
 		return render.hello(name='zbf')

if __name__ == "__main__":
	app.run()
