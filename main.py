# -*- coding: utf-8 -*- 

import web
import urllib2
from handle import Handle

urls=(
	'/wx','Handle',
)


if __name__ == "__main__":

	app = web.application(urls,globals())
	app.run()
