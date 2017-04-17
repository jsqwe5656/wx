# -*- coding: utf-8 -*-

from urllib import request
import json
import os,sqlite3,time

db_file = os.path.join(os.path.dirname(__file__),'token.db')

appID = 'wxe2402d474b877cbb'
appSecret = '14d15d7cb4acedc5771f2d704763efde'
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(appID,appSecret)
print(url)
def url_token():
    with request.urlopen(url) as f:
        data = f.read()
        data = data.decode('utf-8')
        jdata = json.loads(data)
        print(jdata)
        access_token = jdata.get('access_token',None)
        if access_token != None:
            print('not null %s' %access_token)
            set_token(access_token)
        else:
            url_token()
    
#保存token到sqlite数据库中
def set_token(access_token):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    createtime = time.time()
    values = None
    try:
        cursor.execute(r"select *from token where id=1")
        #获得查询结果集
        values = cursor.fetchall()
        print(values)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

   # cursor.execute(r"insert into token(token,createtime) values(%s,%s)" %(access_token,createtime))

    pass

#从数据库中获取token
def get_token():
    pass

if __name__ =='__main__':
    url_token()
    