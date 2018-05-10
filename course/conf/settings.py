"""
    @Time: 2018/5/10 13:55
    @Author: qingyaocui
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB = os.path.join(BASE_DIR, 'db', 'admin')
COURSE_DB = os.path.join(BASE_DIR, 'db', 'course')
SCHOOL_DB = os.path.join(BASE_DIR, 'db', 'school')
STUDENT_DB = os.path.join(BASE_DIR, 'db', 'student')
TEACHER_DB = os.path.join(BASE_DIR, 'db', 'teacher')
CLASSES_DB = os.path.join(BASE_DIR, 'db', 'classes')
COURSE_TO_TEACHER_DB = os.path.join(BASE_DIR, 'db', 'course_to_teacher')