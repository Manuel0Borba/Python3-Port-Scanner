#!/bin/python3

#python3 scanner.py <target_ip> fromport toport   //SCAN FROM fromport TO toport
#python3 scanner.py <target_ip> port   // SCAN ONLY port
#Full port scanner range(1,65535)

import sys
import threading #threading
import socket #make node to node connection
from datetime import datetime as dt
import math 


def Port_scan(target_ip, max_port, i):
	j= i +10 
	if (j > max_port):
		j = max_port # if this surpasses the toport from the inputS, it becomes the input given
	for port in range(i,j): 
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Establish socket
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		socket.setdefaulttimeout(10) #Time untill it gives up, the bigger the interval given the bigger it needs to be
		result = s.connect_ex((target,port)) #Returns error indicator
		if result ==0:
			print("Port {} is open".format(port))
		s.close()


#Define our target
if len(sys.argv) > 2 and len(sys.argv) < 5 :
	target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IPv4
	fromport=int(sys.argv[2])
	toport = int(sys.argv[2])+1
	threads = []

	if len(sys.argv) == 4 :	
		toport = int(sys.argv[3])+1

	try:
		#Add a banner
		print("-" * 50)
		print("Scanning target " + target)
		print("Time started " + str(dt.now()))
		print("-" * 50)
		number_of_threads = math.ceil((toport - fromport + 1)/10)# each Thread will scan 10 ports, except the last one wich will scan <=10 ports
		print("number of threads " + str(number_of_threads ))
		for i in range(number_of_threads):
			t = threading.Thread(target = Port_scan , args=(target, toport, (i*10 +fromport) ))
			threads.append(t)
		for i in range(number_of_threads):
			threads[i].start()

		for i in range(number_of_threads):
			threads[i].join()
	except KeyboarInterrupt:
		print("\nExiting program")
		sys.exit()

	except socket.gaierror:
		print("\nHostname could not be resolved")
		sys.exit()

	except socket.error:
		print("\nCould not connect to server.")
		sys.exit()

else :
		print("Invalid arguments.")
		print("""Syntax: python3 scanner.py <target_ip> fromport toport
	python3 scanner.py <target_ip> port""")
