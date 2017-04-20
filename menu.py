# -*- coding: utf-8 -*-

import urllib
import gettoken

class Menu(object):

    def __init__(self):
        self.accessToken = gettoken.get_token()
        print self.accessToken
    def create(self,postData):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % self.accessToken
        if isinstance(postData,unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl,data=postData)
        data = urlResp.read()
        data = data.decode('utf-8')
        print data

    def query(self):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % self.accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read

    def delete(self):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % self.accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read

    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % self.accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read

if __name__ =='__main__':
    myMenu = Menu()
    postJson = r"""
{
        "button":
        [
            {
                "type": "click",
                "name": "开发指引",
                "key":  "mpGuide"
            },
            {
                "name": "服务",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "更新公告",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "接口权限说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "返回码说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "绑定账号",
                        "url": "http://www.sina.com"
                    }
                ]
            },
            {
                "type": "view",
                "name": "官网",
                "url": "http://www.healforce.com"
            }
          ]
    }
    """
    myMenu.create(postJson)
    #myMenu.query()
    #value = gettoken.get_token()
    #print value