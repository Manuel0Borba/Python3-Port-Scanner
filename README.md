# Python3-Port-Scanner
In this repository you can find a simple port scanner developed in python3 that indicates wich ports are open on a target IPAddress.
It uses Threads to cut down on the scanning time, each scans 10 ports(inside the given interval), except for the last Thread wich scans <= 10 ports.

Simply download the python script and run it as demonstrated:

        python3 scanner.py <target_ipaddress> port1 port2
          -this scans the target_ipaddress ports from port1 to port2 inclusive
          
        python3 scanner.py <target_ipaddress> port1
          -this scans the target_ipaddress port port1
