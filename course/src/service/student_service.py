"""
    @Time: 2018/5/11 10:57
    @Author: qingyaocui
"""
from course.src.service import admin_service
from course.src.models import Student
login_stu = None
def show_choice():
    show = '''
        1.菜单
        2.登录
        3.注册
        4.查看成绩
        Q|q.退出系统
    '''
    print(show)

def login():
    s_name = input('请输入姓名：')
    stu = admin_service.find_student_by_name(s_name)
    if stu:
        global login_stu
        login_stu = stu
        print("登陆成功!")
        print("当前用户: %s" % s_name)
        print(login_stu)
    else:
        print("%s 不存在" % s_name)

def register():
    school_name = input('请输入学校名称:')
    sc = admin_service.find_school_by_name(school_name)
    if sc:
        class_name = input('请输入班级名称：')
        my_class = admin_service.find_class_by_name(class_name)
        if my_class:
            s_name = input('请输入姓名：')
            s_age = input('请输入年龄')
            new_student = Student(s_name, s_age, sc.nid, my_class.nid)
            new_student.save()
            print("%s 学生注册成功!" % s_name)
        else:
            print("班级不存在，注册失败！")

    else:
        print("学校不存在，注册失败！")

def show_score():
    pass

def quit_system():
    print('Bye!')
    exit(0)

def main():
    choice_dict = {
        '1':show_choice,
        '2':login,
        '3':register,
        '4':show_score,
        'Q':quit_system,
        'q':quit_system
    }
    show_choice()
    while True:
        user_input = input("请输入选项:")
        if user_input not in choice_dict:
            print('请输入正确的选项~')
            continue

        option = choice_dict[user_input]
        option()
