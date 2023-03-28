import socket
import sys
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPV4
else:
    print("Invalid amount of args")
    print("Syntax: python3 portscanner.py <ip>")

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\n Exiting Program..")
    sys.exit()

    
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()


except socket.error:
    print("Could not connect to the server.")
    sys.exit()
