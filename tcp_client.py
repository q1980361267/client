import socket
import struct
import time
import json
import xlrd
import select
# 配置文件信息
wb = xlrd.open_workbook('./测试表格.xls')
table = wb.sheet_by_index(0)
ip = table.cell_value(1,1)
port = table.cell_value(2,1)
productId = table.cell_value(3,1)
masterKey = table.cell_value(4,1)
deviceId = table.cell_value(5,1)

#设备连接
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
ip_port = (ip,int(port))
tcp_socket.connect(ip_port)
auth = '*{}#{}#{}*'.format(int(productId),int(deviceId),masterKey)
tcp_socket.sendall(auth.encode())
print('设备鉴权信息： '+ auth)
print('接入机地址： '+ str(ip_port))

# 上报的数据
someString = '{"someString":"ironman"}'
someInteger = '{"someInteger":1234}'
#  上行数据
def upload():
    while True:
        tcp_socket.sendall(struct.pack('!H',len(someString))+someString.encode())
        tcp_socket.sendall(struct.pack('!H',len(someInteger))+someInteger.encode())
        a = struct.pack('!H',len(someString))+someString.encode()
        print('上行数据完成')
        print(a)
        time.sleep(10)
# 下行数据（异步IO）
if __name__ == '__main__':
    # upload()
    inputs = [tcp_socket]
    while True:
        rs,ws,es = select.select(inputs,[],[])
        for r in rs:
           if r is tcp_socket:
                recv = tcp_socket.recv(10240)
                try:
                    recv_dic = json.loads(recv)
                except:
                    continue
                print(recv_dic)
                _uuid = recv_dic['uuid']
                _cmd = recv_dic['cmd']
                _method = recv_dic['method']
                if _method == 'set':
                    _data = _uuid+'success'
                    _len = len(_data)
                    _send = '#'.encode()+struct.pack('!B',_len)+_data.encode()
                    tcp_socket.sendall(_send)
                elif _method == 'get':
                    if _cmd == 'someString':
                        _data = _uuid + 'spiderman'
                        _len = len(_data)
                        _send = '#'.encode() + struct.pack('!B', _len) + _data.encode()
                        tcp_socket.sendall(_send)
                    elif _cmd == 'someInteger':
                        _data = _uuid + '1234'
                        _len = len(_data)
                        _send = '#'.encode() + struct.pack('!B', _len) + _data.encode()
                        tcp_socket.sendall(_send)
                    elif _cmd == 'someFloat':
                        _data = _uuid + '123.123'
                        _len = len(_data)
                        _send = '#'.encode() + struct.pack('!B', _len) + _data.encode()
                        tcp_socket.sendall(_send)
                    elif _cmd == 'someDouble':
                        _data = _uuid + '321.321'
                        _len = len(_data)
                        _send = '#'.encode() + struct.pack('!B', _len) + _data.encode()
                        tcp_socket.sendall(_send)
                    elif _cmd == 'someLong':
                        _data = _uuid + '255000'
                        _len = len(_data)
                        _send = '#'.encode() + struct.pack('!B', _len) + _data.encode()
                        tcp_socket.sendall(_send)
                    elif _cmd == 'someBoolean':
                        _data = _uuid + 'True'
                        _len = len(_data)
                        _send = '#'.encode() + struct.pack('!B', _len) + _data.encode()
                        tcp_socket.sendall(_send)
                    elif _cmd == 'someDate':
                        _data = _uuid + str(int(time.time())*1000)
                        _len = len(_data)
                        _send = '#'.encode() + struct.pack('!B', _len) + _data.encode()
                        tcp_socket.sendall(_send)
