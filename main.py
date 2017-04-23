# -*- coding: utf-8 -*- 

import web
from handle import Handle,SendMessage,Register

urls=(
	'/wx','Handle',
	'/wx/sendmessage','SendMessage',
	'/wx/register','Register'
)


if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
