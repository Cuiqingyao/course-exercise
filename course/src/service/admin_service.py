"""
    @Time: 2018/5/10 15:09
    @Author: qingyaocui
"""
import os
import pickle
from course.src.models import Admin, School, Teacher, Course, Classes
def show_choice():
    show = '''
        1.菜单
        2.创建学校
        3.查看学校
        4.创建老师
        5.创建课程
        6.查看课程
        7.为课程增加老师
        8.创建班级
        Q|q.退出系统
    '''
    print(show)

def create_school():
    '''
    创建学校
    :return:
    '''
    school_name = input('请输入学校的名称：')
    if find_school_by_name(school_name):
        print("学校已经存在！")
        return
    new_school = School(school_name)
    new_school.save()
    print("%s 创建成功！" % school_name)

def show_schools():
    '''
    查看所有学校
    :return:
    '''
    for i in os.listdir(School.db_path):
        with open('%s/%s' % (School.db_path, i), 'rb') as f:
            sc = pickle.load(f)
            print(sc)

def find_school_by_name(school_name):
    '''
    按学校名称查找学校
    :param school_name:学校名称
    :return:
    '''
    for i in os.listdir(School.db_path):
        with open('%s/%s'% (School.db_path, i), 'rb') as f:
            sc = pickle.load(f)
            if sc.school_name == school_name:
                return sc

    return None

def create_teacher():
    '''
    创建老师
    :return:
    '''
    teacher_name = input('请输入老师的姓名：')
    teacher_level = input('请输入老师的等级：')
    school_name = input('请输入老师所在的学校：')
    sc = find_school_by_name(school_name)
    if sc:
        new_teacher = Teacher(teacher_name, teacher_level, sc.nid)
        new_teacher.save()
        sc.add_teacher(new_teacher.nid)
        sc.save()
    else:
        print("学校不存在！老师添加失败！")

def find_teacher_by_name(teacher_name):
    '''
    按姓名查找老师
    :param teacher_name: 老师姓名
    :return:老师集合
    '''
    teachers = []
    for i in os.listdir(Teacher.db_path):
        with open('%s/%s' % (Teacher.db_path, i), 'rb') as f:
            tea = pickle.load(f)
            if tea.teacher_name == teacher_name:
                teachers.append(tea)
    return teachers

def show_teachers(school_name):
    '''
    按学校名称展示师资力量
    :param school_name: 学校名称
    :return:
    '''

    sc = find_school_by_name(school_name)
    if sc:
        sc.show_teachers()
    else:
        print("学校不存在！无法展示老师信息！")



def create_course():
    '''
    创建课程
    :return:
    '''
    school_name = input('请输入要添加课程的学校名称：')
    course_name = input('请输入课程名称：')
    course_price = input('请输入课程价格：')
    course_period = input('请输入课程周期：')
    sc = find_school_by_name(school_name)
    if sc:
        new_course = Course(course_name, course_price, course_period, sc.nid)
        new_course.save()
        sc.add_course(new_course.nid)
        sc.save()
    else:
        print("学校不存在！课程添加失败！")



def show_courses(school_name):
    '''
    按学校名展示课程
    :param school_name:学校名称
    :return:
    '''
    sc = find_school_by_name(school_name)
    if sc:
        sc.show_courses()
    else:
        print('学校不存在！无法展示课程信息！')


def add_teacher_to_course(school_name):
    '''
    按学校名为课程添加教师
    :param school_name: 学校名称
    :return:
    '''
    sc = find_school_by_name(school_name)
    if sc:
        sc.show_courses()
        course_name = input("请输入要添加任课老师的课程名称：")
        for c in sc.courses:
            if c.get_obj_by_uuid().course_name == course_name:
                teacher_name = input('请输入任课老师姓名：')
                for t in sc.teachers:
                    if t.get_obj_by_uuid().teacher_name == teacher_name:
                        c.add_teacher(t.nid)
                        c.save()
                        sc.save()
                        return
                print('老师不存在！')
        print("课程不存在！")
    else:
        print("学校不存在！为课程添加老师失败！")


def create_class():
    '''
    创建班级
    :return:
    '''
    school_name = input('请输入要添加课程的学校名称：')
    class_name = input('请输入课程名称：')
    sc = find_school_by_name(school_name)
    if sc:
        new_class = Classes(class_name, sc.nid)
        new_class.save()
        sc.add_class(new_class.nid)
        sc.save()
    else:
        print("学校不存在！课程添加失败！")


def show_classes(school_name):
    '''
    按学校名展示班级
    :param school_name:学校名
    :return:
    '''
    sc = find_school_by_name(school_name)
    if sc:
        sc.show_classes()
    else:
        print("学校不存在！无法展示班级信息！")


def quit_system():
    print('Bye!')
    exit(0)

def show_login():
    print('选课系统'.center(30,'-'))
    print('管理员接口')
    times_limit = 5
    count = 0
    while True:

        if count < times_limit:
            username = input('请输入[管理员]用户名：')
            password = input('请输入[管理员]密码：')
            if Admin.login(username, password):
                break
            else:
                print('用户名或密码输入错误！请重新输入')
            count += 1
        else:
            quit_system()



def main():

    show_login()
    choice_dict = {
        '1':show_choice,
        '2':create_school,
        '3':show_schools,
        '4':create_teacher,
        '5':create_course,
        '6':show_courses,
        '7':add_teacher_to_course,
        '8':create_class,
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