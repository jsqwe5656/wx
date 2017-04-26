# -*- coding: utf-8 -*- 

import web
from handle import Handle,SendMessage,Register
from web.contrib.template import render_jinja

urls=(
	'/wx','Handle',
	'/wx/sendmessage','SendMessage',
	'/wx/register','Register'
)

render = render_jinja(

)

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
