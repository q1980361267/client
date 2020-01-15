import socket
import select
import queue
import time
# sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建socket实例
# ip_port = ('127.0.0.1',8001)
# sk.bind(ip_port)  #绑定端口
# sk.listen()  #开启监听
# socket,addr = sk.accept()  #重新创建实例socket接收数据报
# data = socket.recv(1024)
# str_data = data.decode('UTF-8')
# print(str_data)
# msg = 'hello client, I am server!'
# socket.send(msg.encode('UTF-8'))
# socket.close()
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
ip_port = ('127.0.0.1',8001)
sk.bind(ip_port)
sk.listen()
inputs =[sk]
outputs =[]
message_queues = {}
while inputs:
    rs,ws,es = select.select(inputs,outputs,[],5)
    for r in rs:
        if r is sk:
            connection,address =  sk.accept()
            print('收到{}连接'.format(address))
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
        else:
            data = r.recv(10240)
            if data != '':
                print('收到{}来的数据：{}'.format(r.getpeername(),data))
                message_queues[r].put(data)
            else:
                print('{} 关闭了连接'.format(r.getpeername()))
                if r in outputs:
                    outputs.remove(r)
                inputs.remove(r)
                r.close()
                del message_queues[r]
    for w in ws:
        try:
            message_queue = message_queues.get(w)
            send_data = ''
            if message_queue is not None:
                send_data = message_queue.get_nowait()
                w.sendall(send_data)
        except queue.Empty:
            print('{} 断开连接'.format(w.getsockname()))

    time.sleep(3)
