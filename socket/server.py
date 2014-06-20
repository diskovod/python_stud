#!/usr/bin/python 

import socket
import errno

class ServerSocket(object):
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ""
        self.port = 8000

    def getConnection(self):
        try:
            self.s.bind((self.host, self.port))
            self.s.listen(5)
            c, addr = self.s.accept()
            print 'Got connection from', addr
            
            c.send("Connected!")



            while True:
                
                data = c.recv(1024)
                if not data: break
                #c.send("GET / HTTP/1.0")
                print data
                
        except socket.error, e:
                print "Error is %s" % (e)
           # c.close()

           
sc = ServerSocket()
sc.getConnection()
