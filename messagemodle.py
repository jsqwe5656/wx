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