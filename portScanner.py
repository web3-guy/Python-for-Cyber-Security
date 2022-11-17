#!/usr/bin/python3

import socket
import sys
import time
import threading


usage = "python3 port_scan.py <target_ip> <start_port> <end_port>"

print("-" * 70)
print("A Simple python port scanner!")
print("-" * 70)


if(len(sys.argv) != 4):
	print(usage)
	sys.exit()


try:
	target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
	print("[-] Name resolution error")
	sys.exit()


start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("[+] Target {}".format(target))
def port_scan(port):
	# print("Scanning port: ", port)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	conn = s.connect_ex((target, port))
	if (not conn):
		print("Port {} is open".format(port))
	s.close

for port in range(start_port, end_port):
	thread = threading.Thread(target= port_scan, args=(port,))
	thread.start()



