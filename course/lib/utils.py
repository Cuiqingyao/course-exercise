"""
    @Time: 2018/5/11 10:01
    @Author: qingyaocui
"""

import time
import uuid
import hashlib


def create_uuid():
    return str(uuid.uuid1())


def create_md5():
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()