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

#使用sdk中的查询方法查看对应公众号是否已被绑定
def query_tel2openid():
    Todo = leancloud.Object.extend('UserInfo')
    query = Todo.query

    query.equal_to('weChat_opeid','o7-Jk0Z-xvOBSUyIcrLZx0PB3FpE')
    query_list = query().find()                     #如果数据库中没有对应条件的查询结果 则会返回[]
    if len(query_list) == 1:
        #TODO
        print 'exits'
    else:
        # TODO
        print 'zbf'

query_tel2openid()

#使用sdk中的查询方法查看对应手机号是否已绑定公众号
def query_tel2openid(tel):
    Todo = leancloud.Object.extend('UserInfo')
    query = Todo.query
    #query.equal_to('userTel','13100871692')
    query.equal_to('userTel', tel)
    query_list = query().find()
    if len(query_list) == 1:
        d = query_list[0].__dict__
        # for k,v in d.items():
        #     print 'dict[%s]=' %k,v
        d2 = d.get('_attributes')
        # for k,v in d2.items():
        #     print 'dict[%s]=' % k, v
        openid = d2.get('weChat_opeid')
        # TODO
        if openid == 'none':
            return d2
        else:
            print '123'
    else:
        #TODO
        print 'TODO'



#query_tel2openid()