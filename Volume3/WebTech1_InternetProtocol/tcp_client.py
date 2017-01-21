#!/usr/bin/env python

import socket


ip = '127.0.0.1'
port = 33498
size = 2048
msg = "It's a beautiful networked world!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(msg)

data = s.recv(size)
print "Received data: ", data
s.close()

