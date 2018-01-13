#!/usr/bin/env python
# coding: utf-8
from socket import *
from time import ctime
import select
import sys

#HOST = '192.168.1.200'
#HOST = '127.0.0.1'
HOST = '207.246.113.233'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)  # 服务器的地址与端口

#HOST = raw_input("Please input host's ip : ")

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 生成客户端的套接字，并连上服务器
tcpCliSock.connect(ADDR)
while True:
    data = raw_input('>>>')
    #print "send"
    tcpCliSock.send (data)
    if data == "exit":
        tcpCliSock.close()
        break
    #tcpCliSock.send('[%s] %s' % (ctime(), data))  # 发送时间与数据
    #print "begin recv..."
    data = tcpCliSock.recv(BUFSIZ)
    #print "recv over..."
    if not data:
        break
    print data

"""
#input1 = [tcpCliSock, sys.stdin]
input1 = [tcpCliSock,sys.stdin]

while True:
    print "6"
    readyInput, readyOutput, readyException = select.select(input1, [], [])
    print "5"
    for indata in readyInput:
        print "4"
        if indata == tcpCliSock:
            print "1"
            data = tcpCliSock.recv(BUFSIZ)
            print "3"
            if not data:
                break
            print data
        else:
            print "2"
            data = raw_input()
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (ctime(), data))  # 发送时间与数据
"""
tcpCliSock.close()