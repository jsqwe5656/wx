# -*- coding: utf-8 -*-

import gettoken,urllib,json,urllib2
from messagemodle import MessageValue

#发送模版消息接口
url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % gettoken.get_token()
print url
#首层json
values = {}
values["touser"]= "o7-Jk0Z-xvOBSUyIcrLZx0PB3FpE"
values["template_id"] = "7MF6StPyTu7nWc5PaFR_XKnGJb9URKfhli0hfsuDcVE"
#模板跳转连接
#values["url"] = ""
#跳小程序所需数据，不需跳小程序可不用传该数据
#values["miniprogram"] = ""
#模板中的data数据
# values["data"] = {"first": {
#                        "value":"血氧测量提醒",
#                        "color":"#173177"
#                    },
#                    "keyword1":{
#                        "value":"2017.04.23 15:42",
#                        "color":"#173177"
#                    },
#                    "keyword2": {
#                        "value":"血氧",
#                        "color":"#173177"
#                    },
#                    "keyword3": {
#                        "value":"血氧值:98% 心率:88bpm",
#                        "color":"#173177"
#                    },
#                     "keyword4": {
#                         "value":"血氧值正常,请继续保持",
#                         "color":"#173177"
#                     },
#                    "remark":{
#                        "value":"",
#                        "color":"#173177"
#                    }}

def send_message(post_json):
    #post_json = json.dumps(values)
    req = urllib2.Request(url,post_json)
    response = urllib2.urlopen(req)
    res = response.read()
    response.close()
    return res

#result = send_message()
#print(result)


value = MessageValue()
value.first = {"value":"血氧测量提醒","color":"#173177"}
value.keyword1 = {"value":"血氧测量提醒","color":"#173177"}
value.keyword2 = {"value":"血氧测量提醒","color":"#173177"}
value.keyword3 = {"value":"血氧测量提醒","color":"#173177"}
value.keyword4 = {"value":"血氧测量提醒","color":"#173177"}
value.remark = {"value":"血氧测量提醒","color":"#173177"}
dvalue = value.__dict__
print(dvalue)
jvalue = json.dumps(dvalue)
print type(jvalue)
print jvalue


