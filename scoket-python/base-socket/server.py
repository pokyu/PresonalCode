#!/usr/bin/env python
# -*-coding:utf-8-*-

from socket import *
from time import ctime
import select
import sys,os

HOST = ''
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
#input = [tcpSerSock, sys.stdin] ##非windows环境，使用这条，可用select监控输入
input = [tcpSerSock]

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr
    input.append(tcpCliSock)  # 不同的就在这里，当有客户端连接时，要把他加进input

    while True:
        readyInput, readyOutput, readyException = select.select(input, [], [])  # 每次循环都会阻塞在这里，只有当有数据输入时才会执行下面的操作
        print "s"
        for indata in readyInput:
            if indata == tcpCliSock:
                data = tcpCliSock.recv(BUFSIZ)
                if not data:
                    break
                print data
                if data == "exit":
                    tcpCliSock.close()
                    break
                res = os.popen(data.decode()).read()
                #print "result : %s" % (res)
                if len(res) == 0:
                    res = "cmd has no output..."
                #tcpCliSock.send(str(len(res.encode('utf-8'))).encode('utf-8'))
                tcpCliSock.send(res.encode('utf-8'))
                #tcpCliSock.sendall( "recv data:%s" % (data) )
            else:
                data = raw_input()
                if not data:
                    break
                tcpCliSock.send('[%s] %s' % (ctime(), data))

tcpCliSock.close()