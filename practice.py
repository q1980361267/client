# with open('测试文件.txt','r') as f:
#     # f.write('\n这个总是一个测试文件')
#     arry = f.readlines()
#     data = [line.strip('\n') for line in arry]
#     print(data)
#     f.close()
# import struct
# buff = struct.pack('ii',4,4)
# str = struct.unpack('q',buff)
# print(buff)
# import json
# data = ['a','b','c']
# data_trasform = json.dumps(data)
# print(type(data))
# print(type(data_trasform))

#获取表单数据
# import xlrd
# data = xlrd.open_workbook('./测试表格.xls')
# table = data.sheet_by_index(0)
# value = table.col_values(0)
# someData = table.cell_value(1,1)
# print(type(someData))
# print(table)

#设置颜色
# from colorama import Fore,Back,Style,init
# init(autoreset=True)
# print(Fore.CYAN+ 'Welcome to python!!'+ Fore.RESET)
# print('automatically back to default ')

# import select
# array = [1,2,3,4,5,6,7,8,9,10]
# solved_array = select.select([array<6],[array+1],100)
# print(solved_array)

# import os
# print(os.name)
# import queue
# q = queue.Queue()
# for a in range(5):
#     q.put(a)
# dic = {'a':q}
# b = dic.get(q)
# print(b)
# dics = {'a':1,
#        'b':2,
#        'c':3
#        }
# dic = dics.get(1)
# print(dic)

# a = '{}是用来替换的标识符'.format('%s')
# print(a)
#
# import queue
# a = queue.LifoQueue()
# for i in range(5):
#     a.put(i)
# print(a.get_nowait())
import xlrd
wb = xlrd.open_workbook('./测试表格.xls')
table = wb.sheet_by_index(0)
ip = table.cell_value(1,1)
port = table.cell_value(2,1)
productId = table.cell_value(3,1)
masterKey = table.cell_value(4,1)
deviceId = table.cell_value(5,1)
print(type(ip))
print(port)