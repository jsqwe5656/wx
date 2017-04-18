# -*- coding: utf-8 -*- 

import web,gettoken
from handle import Handle

urls=(
	'/wx','Handle',
)


if __name__ == "__main__":
	value = gettoken.get_token()
	print value
	app = web.application(urls,globals())
	app.run()
