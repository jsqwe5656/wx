# -*- coding: utf-8 -*-

from urllib import request
from collections import defaultdict
import json

appID = 'wxe2402d474b877cbb'
appSecret = '14d15d7cb4acedc5771f2d704763efde'
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(appID,appSecret)
url = 'https://api.douban.com/v2/book/2129650'
print(url)
with request.urlopen(url) as f:
    print(f.status,f.reason)
    data = f.read()
    for key,value in f.getheaders():
        print('%s = %s'%(key,value))
    data = data.decode('utf-8')
    #print('Data:',data)
    jdata = json.loads(data)
    print(jdata)
    print(defaultdict(jdata['zbf'],0))
    

