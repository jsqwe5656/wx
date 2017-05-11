# -*- coding: utf-8 -*-
'处理绑定手机号的逻辑'

import urllib2,json
import leancloud
import gettoken
from messagemodle import ResultModle


leancloud.init('KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz','TNpBJHMPmG2lVGbTJeVkHUgE')

class Result(dict):
    def __int__(self):
        self.code = None
        self.message = None
        self.objectID = None
        self.tellNumber = None
        self.openID = None

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s',by zbf" %key)

    def __setattr__(self, key, value):
        self[key] = value

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
    result = ResultModle()
    data = response.read()
    if len(data) == 2:
        result.errorcode = 30000
        result.errmsg = u'success'
        dresult = result.__dict__
        jresult = json.dumps(dresult)
        return jresult
    else:
        return data

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
        result.openID = openid
    #dresult = result.__dict__
    #jresult = json.dumps(dresult)
    return result

#使用sdk中的查询方法查看对应手机号是否已绑定公众号 输入手机号之后发送的请求
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
        #    print 'dict[%s]=' % k, v
        openID = d2.get('weChat_openid')
        if openID == 'none':
            return get_smx(tel)
        else:
            result = ResultModle()
            result.errorcode = 30051
            result.errmsg = 'openid is exist'
            dresult = result.__dict__
            print (dresult)
            jresult = json.dumps(dresult)
            print (jresult)
            return jresult
    else:
        return get_smx(tel)


#更新userinfo表中的openid
def update_save2openid(result):
    Todo = leancloud.Object.extend('UserInfo')
    to = Todo.create_without_data(result.objectID)
    to.set('weChat_openid',result.openID)
    return to.save()

#根据code获取用户的openid
def getopenid(code):
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code'%(gettoken.appID,gettoken.appSecret,code)
    #request = urllib2(url)
    response = urllib2.urlopen(url)
    #jdata = json.dumps(response)
    data = response.read()
    ddata = json.loads(data)
    print (ddata.get('openid'))
    openid = ddata.get('openid')
    return openid

# result = Result()
# result.openID = 'o7-Jk0Z-xvOBSUyIcrLZx0PB3FpE'
# result.objectID = '5859faec61ff4b0063dd3b13'
# print update_save2openid(result)

#getopenid('061BTTlg10oCRv0DIlng1ZU4mg1BTTlU')

