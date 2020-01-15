import socket
import random
import time
import struct
# sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ip_port = ('127.0.0.1',8001)
# str_data = 'hello world! '
# sk.connect(ip_port)
# data_str = input('请输入想发给服务器的话：')
# sk.send(data_str.encode('UTF-8'))
# data = sk.recv(1024)
# print(data.decode('UTF-8'))
# sk.close()

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
server_port = ('127.0.0.1',8001)
sk.connect(server_port)
while True:
    data = random.randint(1,100)
    send_data = struct.pack('!B',data)
    sk.sendall(send_data)
    time.sleep(1)
    # rec_data = sk.recv(10240)
    # print('接收到服务器的数据： ' + rec_data.decode())
