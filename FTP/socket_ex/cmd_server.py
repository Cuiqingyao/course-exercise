"""
    @Time: 2018/5/16 10:35
    @Author: qingyaocui
"""

import subprocess
import socket

server_addr = ('127.0.0.1', 8000)

sk = socket.socket()

sk.bind(server_addr)

sk.listen(3)

while True:
    conn,_ = sk.accept()
    print('连接成功！', conn)
    while True:
        print('等待发送命令！')
        try:
            recv_f_c = conn.recv(1024)
        except Exception as e:
            print("客户端意外终止")
            break
        else:
            if str(recv_f_c, 'utf8') == 'exit':
                print("客户端正常退出")
                break
        cmd = str(recv_f_c, 'utf8')
        print("执行 %s" % cmd)
        cmd_result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
        res_len = len(cmd_result)
        conn.send(bytes('%d'%res_len, 'utf8'))
        conn.recv(1024)
        conn.sendall(cmd_result)
    if not conn:
        conn.close()