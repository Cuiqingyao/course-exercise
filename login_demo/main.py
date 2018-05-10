"""
    @Time: 2018/5/8 19:03
    @Author: qingyaocui
"""
import os
import sys
from data_helper import load_userdata

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

auth_status = False

def menu():
    user_operation = {
        '1' : 'home()',
        '2' : 'finance()',
        '3' : 'book()',
        'q' : 0,
        'Q' : 0
    }
    while True:
        print('welcome to the JD!'.center(30, '-'))
        print('1. home page')
        print('2. finance page')
        print('3. book page')
        print('Q/q. exit')
        user_input = input('>>:')
        if user_input == 'q' or user_input == 'Q':
            exit(user_operation[user_input])
        if user_input in user_operation:
            eval(user_operation[user_input])
        else:
            print('please input correct options ~')

def login(auth_type):
    '''
    登录验证
    :param auth_type:验证类型
    :return: 验证装饰器函数
    '''
    def check(f):

        data = load_userdata(auth_type)
        def inner():

            global auth_status
            if auth_status == False:
                while True:
                    username = input('please input %s name >>: ' % (auth_type))
                    password = input('please input %s password >>: ' % (auth_type))
                    if username.strip() == data['username'] and password.strip() == data['password']:

                        auth_status = True
                        f()
                        return
                    else:
                        print('incorrect username or password!')
            else:
                f()
        return inner

    return check


@login('jd_user') # home = check(home)
def home():
    print('home page!!')

@login('wx_user')
def finance():
    print('finance page!!')

@login('jd_user')
def book():
    print('book page!!')

if __name__ == '__main__':
    menu()