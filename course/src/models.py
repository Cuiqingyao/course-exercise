"""
    @Time: 2018/5/10 14:03
    @Author: qingyaocui
"""

import pickle
import time
import os
import pickle
from course.src import identifier
from course.conf import settings


class BaseModel:

    def save(self):
        '''
        使用pickle 序列化 用户对象
        :return:
        '''
        nid = str(self.nid)
        file_path = os.path.join(self.db_path, nid)
        pickle.dump(self, open(file_path, 'wb'))

class School(BaseModel):
    db_path = settings.SCHOOL_DB

    def __init__(self, name):
        self.nid = identifier.SchoolNid(School.db_path)
        self.school_name = name
        self.income = 0
        self.courses = []
        self.teachers = []
        self.classes = []

    def __str__(self):
        return self.school_name

    def add_teacher(self, teacher_nid):
        '''
        为此学校添加老师
        :param teacher:老师
        :return:
        '''
        self.teachers.append(teacher_nid)

    def add_course(self, course_nid):
        '''
        为此学校添加课程
        :param course:课程
        :return:
        '''
        self.courses.append(course_nid)

    def add_class(self, new_class_nid):
        '''
        为此学校添加班级
        :param new_class:班级
        :return:
        '''
        self.classes.append(new_class_nid)

    def show_teachers(self):
        '''
        查看此学校师资力量
        :return:
        '''
        if len(self.teachers):
            print('%s 师资力量：' % self.school_name)
            for teacher_nid in self.teachers:
                print(teacher_nid.get_obj_by_uuid())
        else:
            print('%s 还未招收老师!' % (self.school_name))

    def show_courses(self):
        '''
        查看此学校开设的课程
        :return:
        '''
        if len(self.courses):
            print('%s 开设了一下课程：' % self.school_name)
            for course_nid in self.courses:
                print(course_nid.get_obj_by_uuid())
        else:
            print('%s 还未开设课程!' % (self.school_name))

    def show_classes(self):
        '''
        查看此学校的所有班级
        :return:
        '''
        if len(self.classes):
            print('%s 有以下班级：' % self.school_name)
            for new_class_nid in self.classes:
                print(new_class_nid.get_obj_by_uuid())
        else:
            print('%s 还为开设班级!' % (self.school_name))


class Teacher(BaseModel):
    db_path = settings.TEACHER_DB

    def __init__(self, name, level, school_nid):
        self.nid = identifier.TeacherNid(Teacher.db_path)
        self.teacher_name = name
        self.teacher_level = level
        self.school_nid = school_nid
        self.__account = 0

    def __str__(self):
        return ','.join(['[Teacher] name:%s' % (self.teacher_name),
                         'level:%s' % (self.teacher_level),
                         'working at:%s' % (self.school_nid.get_obj_by_uuid().school_name)])



class Course(BaseModel):
    db_path = settings.COURSE_DB

    def __init__(self, name, price, period, school_id):
        self.nid = identifier.CourseNid(Course.db_path)
        self.course_name = name
        self.course_price = price
        self.course_period = period
        self.school_id = school_id
        self.teachers = []
    def __str__(self):
        return ','.join(['course name:%s' % (self.course_name),
                         'course price:%s' % (self.course_price),
                         'course period:%s' % (self.course_period),
                         'course in schoole:%s' % (self.school_id.get_obj_by_uuid().school_name)])
    def add_teacher(self, teacher_nid):

        self.teachers.append(teacher_nid)

    def show_teachers(self):

        if len(self.teachers):
            print('%s 有以下任课老师：' % self.course_name)
            for tea_nid in self.teachers:
                print(tea_nid.get_obj_by_uuid())
        else:
            print('%s 还没有任课老师!' % (self.course_name))



class Admin(BaseModel):
    db_path = settings.ADMIN_DB

    def __init__(self, username, password):
        '''
        创建管理员对象
        :param username:
        :param password:
        '''
        self.nid = identifier.AdminNid(Admin.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')

    @staticmethod
    def login(username, password):

        for i in os.listdir(Admin.db_path):
            admin_obj = None
            with open('%s/%s'%(Admin.db_path, i), 'rb') as f:
                admin_obj = pickle.load(f)
            if admin_obj.username == username and admin_obj.password == password:
                return True
        return False

class Score:
    def __init__(self, student_id):
        self.student_id = student_id
        self.score_dict = {}

    def set(self, course_to_teacher_nid, number):
        self.score_dict[course_to_teacher_nid] = number

    def get(self, course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid)



class Student(BaseModel):
    db_path = settings.STUDENT_DB

    def __init__(self, name, age, school_id, classes_id):
        self.nid = identifier.StudentNid(Student.db_path)
        self.student_name = name
        self.student_age = age
        self.school_id = school_id
        self.classes_id = classes_id
        self.score = Score(self.nid)

    def __str__(self):
        return ','.join(['[Student] name:%s' % (self.student_name),
                         'age:%d' % (self.student_age),
                         'at school:%s' % (self.school_id.get_obj_by_uuid().school_name),
                         'at class:%s' % (self.classes_id.get_obj_by_uuid().class_name)])

    @staticmethod
    def register():
        pass

class Classes(BaseModel):
    db_path = settings.CLASSES_DB

    def __init__(self, name, school_id):
        self.nid = identifier.ClassesNid(Classes.db_path)
        self.class_name = name
        self.school_id = school_id
        self.students = []

    def __str__(self):
        return ','.join(['[Class] name:%s' % (self.class_name),
                         'at school:%s' % (self.school_id.get_obj_by_uuid().school_name),
                         'has member:%d' % (len(self.students))])


