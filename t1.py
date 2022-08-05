#!/usr/bin/env python2

from socket import *
import time
import base64
import sys
import struct

host=sys.argv[1]
port=25

sock=socket(AF_INET,SOCK_STREAM)
sock.connect((host,port))
print sock.recv(1000)

sock.sendall('EHLO example.com\n')
print sock.recv(1000)

s='AUTH PLAIN\n'
sock.sendall(s)
print sock.recv(1000)

sock.sendall('dGVzdAB0ZXN0ADEyMzQ=\n')
print sock.recv(10000)

sock.close()


