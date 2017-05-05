# -*- coding: utf-8 -*-
'处理绑定手机号的逻辑'

import urllib2,json
import leancloud


leancloud.init('KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz','TNpBJHMPmG2lVGbTJeVkHUgE')

class Result(object):
    def __int__(self):
        self.code = None
        self.message = None
        self.objectID = None
        self.tellNumber = None
        self.openID = None

# 获取验证码
def get_smx(tel):
    url = 'https://api.leancloud.cn/1.1/requestSmsCode'
    request = urllib2.Request(url)
    request.add_header('X-LC-Id','KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz')
    request.add_header('X-LC-Key','TNpBJHMPmG2lVGbTJeVkHUgE')
    request.add_header('Content-Type', 'application/json')
    postdata = {"mobilePhoneNumber": str(tel)}
    jdata = json.dumps(postdata)
    response = urllib2.urlopen(request,jdata)
    return response.read()

#校验验证码
def check_sms(tel,snscode):
    url2 = 'https://api.leancloud.cn/1.1/usersByMobilePhone'
    request2 = urllib2.Request(url2)
    request2.add_header('X-LC-Id','KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz')
    request2.add_header('X-LC-Key','TNpBJHMPmG2lVGbTJeVkHUgE')
    request2.add_header('Content-Type', 'application/json')
    postdata2 = {"mobilePhoneNumber": str(tel),"smsCode":str(snscode)}
    jdata2 = json.dumps(postdata2)
    response2 = urllib2.urlopen(request2,jdata2)
    return response2.read()

#使用sdk中的查询方法查看对应公众号是否已被绑定 进入界面需要发送的请求
def query_openid2exist(openid):
    Todo = leancloud.Object.extend('UserInfo')
    query = Todo.query

    query.equal_to('weChat_openid',str(openid))
    query_list = query().find()    #如果数据库中没有对应条件的查询结果 则会返回[]
    result = Result()
    if len(query_list) == 1:
        result.code = 1
        result.message = 'openid exist'
    else:
        result.code = 0
        result.message = 'no openid exist'
    dresult = result.__dict__
    jresult = json.dumps(dresult)
    return jresult

#使用sdk中的查询方法查看对应手机号是否已绑定公众号 输入手机号之后发送的请求
def query_tel2openid(tel):
    Todo = leancloud.Object.extend('UserInfo')
    query = Todo.query
    #query.equal_to('userTel','13100871692')
    query.equal_to('userTel', tel)
    query_list = query().find()

    result = Result()
    if len(query_list) == 1:
        d = query_list[0].__dict__
        for k,v in d.items():
            print 'dict[%s]=' %k,v
        d2 = d.get('_attributes')
        for k,v in d2.items():
           print 'dict[%s]=' % k, v
        openID = d2.get('weChat_openid')
        if openID == 'none':
            return get_smx(tel)
        else:
            result.tellNumber = d2.get('userTel')
            result.objectID = d2.get('objectId')
            result.code = 1
            result.message = 'openid is exist'
            dresult = result.__dict__
            jresult = json.dumps(dresult)
            return jresult
    else:
        return get_smx(tel)


#更新userinfo表中的openid
def update_save2openid(result):
    Todo = leancloud.Object.extend('UserInfo')
    to = Todo.create_without_data(result.objectID)
    to.set('weChat_openid',result.openID)
    return to.save()

result = Result()
result.openID = 'o7-Jk0Z-xvOBSUyIcrLZx0PB3FpE'
result.objectID = '5859faec61ff4b0063dd3b13'
print update_save2openid(result)

