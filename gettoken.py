# -*- coding: utf-8 -*-

import urllib2
import json
import os,sqlite3,time

db_file = os.path.join(os.path.dirname(__file__),'token.db')

appID = 'wxe2402d474b877cbb'
appID = 'wx34ebef966ed60eef'
appID = 'wx4536896b8007ed7e'
appSecret = '14d15d7cb4acedc5771f2d704763efde'
appSecret = '5aa11ef6fa390d1f6d72839cfbb8467b'
appSecret = '1c5a4ac37d02b31a448bec9f0629b957'
url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' %(appID,appSecret)
print(url)

def url_token():
    f = urllib2.urlopen(url)
    data = f.read()
    data = data.decode('utf-8')
    jdata = json.loads(data)
    print(jdata)
    access_token = jdata.get('access_token',None)
    if access_token != None:
        set_token(access_token)
    else:
        url_token()
    f.close()
    
#保存token到sqlite数据库中
def set_token(access_token):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    createtime = time.time()
    try:
        sql = "update token set token=\"%s\",createtime=\"%s\" where id=1" %(access_token,createtime)
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e.args)
    finally:
        cursor.close()
        conn.close()

#从数据库中获取token
def get_token():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        cursor.execute(r"select *from token where id=1")
        values = cursor.fetchall()
        return check_time(values)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#判断上次获取token的时间是否超过2小时 默认有效期为7200秒
def check_time(values):
    time_now = time.time()
    time_db = float(values[0][2])
    time_difference = time_now - time_db
    print time_difference
    if time_difference > 3600:
        url_token()
        return get_token()
    else:
        return values[0][1]

if __name__ =='__main__':
    #url_token()
    vaule = get_token()
    print vaule
    