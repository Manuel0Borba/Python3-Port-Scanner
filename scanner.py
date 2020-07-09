#!/bin/python3

#python3 scanner.py <target_ip> fromport toport   //SCAN FROM fromport TO toport
#python3 scanner.py <target_ip> port   // SCAN ONLY port

import sys
import socket #make node to node connection
from datetime import datetime as dt

#Define our target
if len(sys.argv) > 2 and len(sys.argv) < 5 :
	target = socket.gethostbyname(sys.argv[1]) #Translate Hostname to IPv4
	fromport=int(sys.argv[2])
	toport = int(sys.argv[2])+1

	if len(sys.argv) == 4 :	
		toport = int(sys.argv[3])+1

	try:
		#Add a banner
		print("-" * 50)
		print("Scanning target " + target)
		print("Time started " + str(dt.now()))
		print("-" * 50)
		for port in range(fromport,toport): #Full port scanner range(1,65535)
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Establish socket
			socket.setdefaulttimeout(1) #Time untill it gives up
			result = s.connect_ex((target,port)) #Returns error indicator
			if result ==0:
				print("Port {} is open".format(port))
			s.close()

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
