# -*- coding: utf-8 -*-

#测量消息模版对象
class MessageValue(object):
    def __init__(self):
        self.first = None
        self.keyword1 = None
        self.keyword2 = None
        self.keyword3 = None
        self.keyword4 = None
        self.remark = None

#模板消息对象 无关联小程序 所以不添加app and不需要跳转所以不加url
class MessageModle(object):
    def __init__(self):
        self.touser = None
        self.template_id = None
        self.data = None

#返回消息对象跟微信统一
class ResultModle(object):
    def __init__(self):
        self.errorcode = None
        self.errmsg = None
        self.msgid = None

#接受的健康数据
class HealthMessage(object):
    def __init__(self):
        self.phoneNumber = None         #电话号
        self.openID = None              #公众号对应的唯一openid
        self.messageMode = None         #数据类型 血氧、血压
        self.data = None                #具体数值

class HealthData(object):
    def __init__(self):
        self.message = None
        self.time = None
        self.bmp = None

#血氧数值
class BOData(HealthData):
    def __init__(self):
        self.spo2 = None
        self.pi = None

#血压数值
class BPMdata(HealthData):
    def __init__(self):
        self.high = None
        self.low = None


