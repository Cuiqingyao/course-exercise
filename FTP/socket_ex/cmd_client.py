"""
    @Time: 2018/5/16 10:44
    @Author: qingyaocui
"""

# import socket
#
# sk = socket.socket()
#
# address = ('127.0.0.1', 8000)
#
# sk.connect(address)
#
# data = sk.recv(1024)
#
# print(str(data, encoding='utf8'))
# sk.s

import socket

sk = socket.socket()

server_addr = ('127.0.0.1', 8000)

sk.connect(server_addr)

while True:
    cmd = input('$:')
    sk.send(bytes(cmd, 'utf8'))
    if cmd == 'exit':
        break
    info = sk.recv(1024)
    print(info)
    res_len = int(str(info, 'gbk'))
    sk.send(bytes('ok', 'utf8'))
    data = bytes()
    while len(data) != res_len:
        recv_f_s = sk.recv(1024)
        data += recv_f_s

    print(str(data, 'gbk'))

sk.close()