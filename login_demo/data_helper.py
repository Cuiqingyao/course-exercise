"""
    @Time: 2018/5/8 18:43
    @Author: qingyaocui
"""
import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


jd_user = {
    'username' : 'jd_123',
    'password' : 'jd'
}

wx_user = {
    'username' : 'wx_123',
    'password' : 'wx'
}

user_type = {'jd_user':jd_user, 'wx_user':wx_user}

def dump_userdata(data, user_type):
    with open('./%s.json' % (user_type), 'w') as f:
        json.dump(data, f)
def load_userdata(user_type):
    with open('./%s.json' % (user_type), 'r') as f:
        data = json.load(f)
    return data
if __name__ == '__main__':

    for i in user_type:
        dump_userdata(data=user_type[i], user_type=i)
    data = load_userdata('jd_user')
    print(type(data),data)
    pass
