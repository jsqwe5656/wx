# -*- coding: utf-8 -*-

import urllib
import gettoken

class Menu(object):

    def __init__(self):
        self.accessToken = gettoken.get_token()

    def create(self,postData):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % self.accessToken
        if isinstance(postData,unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl,data=postData)
        print urlResp.read

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
    postJson = """
    {
    "button": [
        {
            "type": "click", 
            "name": "今日歌曲", 
            "key": "V1001_TODAY_MUSIC"
        }, 
        {
            "type": "click", 
            "name": "歌手简介", 
            "key": "V1001_TODAY_SINGER"
        }, 
        {
            "name": "菜单", 
            "sub_button": [
                {
                    "type": "click", 
                    "name": "hello word", 
                    "key": "V1001_HELLO_WORLD"
                }, 
                {
                    "type": "click", 
                    "name": "赞一下我们", 
                    "key": "V1001_GOOD"
                }
            ]
        }
    """
    myMenu.create(postJson)
