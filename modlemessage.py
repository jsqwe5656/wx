# -*- coding: utf-8 -*-

import gettoken,urllib,json,urllib2

#发送模版消息接口
url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % gettoken.get_token()
print url
#首层json
values = {}
values["touser"]= "o7-Jk0Z-xvOBSUyIcrLZx0PB3FpE"
values["template_id"] = "5TvD5BHmeSz-S0e0h4QK8YAZPpL320XdLjoojfGuG_A"
#模板跳转连接
#values["url"] = ""
#跳小程序所需数据，不需跳小程序可不用传该数据
#values["miniprogram"] = ""
#模板中的data数据
values["data"] = {"first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
                   "keyword1":{
                       "value":"巧克力",
                       "color":"#173177"
                   },
                   "keyword2": {
                       "value":"39.8元",
                       "color":"#173177"
                   },
                   "keyword3": {
                       "value":"2014年9月22日",
                       "color":"#173177"
                   },
                   "remark":{
                       "value":"欢迎再次购买！",
                       "color":"#173177"
                   }}

post_json = json.dumps(values)
req = urllib2.Request(url,post_json)
response = urllib2.urlopen(req)
res = response.read()
response.close()
print(res)

