# -*- coding: utf-8 -*-

import urllib2,json
import leancloud

leancloud.init('KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz','TNpBJHMPmG2lVGbTJeVkHUgE')


# 获取验证码
def get_smx():
    url = 'https://api.leancloud.cn/1.1/requestSmsCode'
    request = urllib2.Request(url)
    request.add_header('X-LC-Id','KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz')
    request.add_header('X-LC-Key','TNpBJHMPmG2lVGbTJeVkHUgE')
    request.add_header('Content-Type', 'application/json')
    postdata = {"mobilePhoneNumber": "13100871692"}
    jdata = json.dumps(postdata)
    response = urllib2.urlopen(request,jdata)
    return response.read()
#校验验证码
def check_sms():
    url2 = 'https://api.leancloud.cn/1.1/usersByMobilePhone'
    request2 = urllib2.Request(url2)
    request2.add_header('X-LC-Id','KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz')
    request2.add_header('X-LC-Key','TNpBJHMPmG2lVGbTJeVkHUgE')
    request2.add_header('Content-Type', 'application/json')
    postdata2 = {"mobilePhoneNumber": "13100871692","smsCode":"318453"}
    jdata2 = json.dumps(postdata2)
    response2 = urllib2.urlopen(request2,jdata2)
    return response2.read()

#查询
def query():
    url = 'https://api.leancloud.cn/1.1/classes/UserInfo'
    request = urllib2.Request(url)
    request.add_header('X-LC-Id','KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz')
    request.add_header('X-LC-Key','TNpBJHMPmG2lVGbTJeVkHUgE')
    request.add_header('Content-Type', 'application/json')
    #postdata = {"where":{"userTel":"13100871692"}}
    #postdata = u'where={"userTel":"13100871692"}'
    response = urllib2.urlopen(request)
    print response.read()

#query()

def query_sdk():
    pass
