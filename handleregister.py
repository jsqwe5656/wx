# -*- coding: utf-8 -*-
'处理绑定手机号的逻辑'

import urllib2,json
import leancloud
import gettoken
from messagemodle import ResultModle


leancloud.init('KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz','TNpBJHMPmG2lVGbTJeVkHUgE')

#接口统一返回类
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

#电话号未被注册验证验证码后添加到userinfo中
def save_tel2userinfo(result):
    TodoFolder = leancloud.Object.extend('UserInfo')
    todo_folder = TodoFolder()
    todo_folder.set('userID', result.objectID)
    todo_folder.set('userTel', result.tellNumber)
    todo_folder.save()
    #将_User表中的id 改成 保存成功后的 userinfo 中的 objectID
    result.objectID = todo_folder.id
    print update_save2openid(result)

#查询电话号是否已被注册
def query_tel2exist(result):
    Todo = leancloud.Object.extend('UserInfo')
    query = Todo.query

    query.equal_to('userTel',result.tellNumber)
    query_list = query().find()    #如果数据库中没有对应条件的查询结果 则会返回[]
    if len(query_list) == 1:
        return                    #userinfo表中已有
    else:
        save_tel2userinfo(result)

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
def check_sms(result):
    url2 = 'https://api.leancloud.cn/1.1/usersByMobilePhone'
    #url2 = "https://api.leancloud.cn/1.1/verifySmsCode/%s?mobilePhoneNumber=%s" % (result.code,result.tellNumber)
    print url2
    request2 = urllib2.Request(url2)
    request2.add_header('X-LC-Id','KHU4OSb7llLkhNDkIcT5BKJc-gzGzoHsz')
    request2.add_header('X-LC-Key','TNpBJHMPmG2lVGbTJeVkHUgE')
    request2.add_header('Content-Type', 'application/json')
    postdata2 = {"mobilePhoneNumber": str(result.tellNumber),"smsCode":str(result.code)}
    jdata2 = json.dumps(postdata2)
    response2 = urllib2.urlopen(request2,jdata2)
    #response2 = urllib2.urlopen(request2)
    data = response2.read()
    print data
    ddata = json.loads(data)
    check_result = Result()
    check_result.tellNumber = ddata.get('mobilePhoneNumber')
    check_result.openID = ddata.get('objectId')
    query_tel2exist(check_result)
    return response2.read()
    #return update_save2openid(result)

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
result = Result()
result.tellNumber = '13100871692'
result.code = 318453
print(check_sms(result))

