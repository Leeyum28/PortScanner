#!/bin/python
import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print('invalid amount of arguments')

print('-' * 50)
print("scanning target: " + target)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f'port {port} is open')
		s.close
	
except KeyboardInterrupt:
	print('exiting program')
	sys.exit()
except socket.error:
	print('cant connect')
	sys.exit()