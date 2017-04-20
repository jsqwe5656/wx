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
 	"button":[
 	{	
    	"type":"click",
    	"name":"今日歌曲",
     	"key":"V1001_TODAY_MUSIC" 
	},
	{ 
		"name":"菜单",
		"sub_button":[
		{	
			"type":"view",
			"name":"搜索",
			"url":"http://www.soso.com/"
		},
		{
			"type":"view",
			"name":"视频",
			"url":"http://v.qq.com/"
		},
		{
			"type":"click",
			"name":"赞一下我们",
			"key":"V1001_GOOD"
		}]
 }],
"matchrule":{
  "group_id":"2",
  "sex":"1",
  "country":"中国",
  "province":"广东",
  "city":"广州",
  "client_platform_type":"2"
  "language":"zh_CN"
  }
}
    """
    myMenu.create(postJson)
    #value = gettoken.get_token()
    #print value