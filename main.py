# -*- coding: utf-8 -*- 

import web

urls=(
	'/wx','Handle',
)


if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
