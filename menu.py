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
                "name": "微产品",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "血氧仪",
                        "url": "http://h.eqxiu.com/s/OGEEizse"
                    },
                    {
                        "type": "view",
                        "name": "心电仪",
                        "url": "http://eqxiu.com/s/dMCHHVRc"
                    },
                    {
                        "type": "view",
                        "name": "血压计",
                        "url": "http://eqxiu.com/s/nsReVv3a"
                    },
                    {
                        "type": "view",
                        "name": "雾化器",
                        "url": "http://eqxiu.com/s/IEorAr0D"
                    },
                    {
                        "type": "view",
                        "name": "防雾霾口罩",
                        "url": "http://c.eqxiu.com/s/1uYZ4mOV"
                    }
                ]
            },
            {
                "name": "服务",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "售后服务",
                        "url": "http://www.healoo.com/index.php?ac=article&at=list&tid=245"
                    },
                    {
                        "type": "view",
                        "name": "问题反馈",
                        "url": "http://www.healoo.com/index.php?ac=form&at=list&fgid=1"
                    },
                    {
                        "type": "view",
                        "name": "软件下载",
                        "url": "http://www.healoo.com/index.php?ac=article&at=list&tid=253"
                    },
                    {
                        "type": "view",
                        "name": "绑定账号",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxa18fb38adf638832&redirect_uri=http%3a%2f%2fjiayong.healoo.com%2fwx%2fregister&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect"
                    }
                ]
            },
            {
                "name": "旗舰店",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "京东官方旗舰店",
                        "url": "https://healforce.jd.com/"
                    }
                ]
            }
          ]
    }
    """
    #"url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxa18fb38adf638832&redirect_uri=http%3a%2f%2fjiayong.healoo.com%2fwx%2fregister&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect"
    #"url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxa18fb38adf638832&redirect_uri=http%3a%2f%2fjiayong.healoo.com%2fwx%2fregister&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
    myMenu.create(postJson)
    #myMenu.query()
    #value = gettoken.get_token()
    #print value