#!/usr/bin/python

import socket
import sys
import traceback

class ClientConnection(object):
    def __init__(self):
        self.host = 'www.pythonstud.com'
        self.port = 80
        self.message = "GET / HTTP/1.0 \nHost: www.pythonstud.com \nConnection: close\r\n\r\n"
        self.message_1 =  "GET / HTTP/1.0 \nHost: www.pythonstud.com/test.html\r\n\r\n"

    def connectToServer(self):

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout( 5.0)

        except socket.error, msg:
            print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
            sys.exit();
 
        print 'Socket Created'
  
        try:
            remote_ip = socket.gethostbyname( self.host )
 
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
     
        #print 'Ip address of ' + self.host + ' is ' + remote_ip
 
        s.connect((remote_ip , self.port))
 
        print 'Socket Connected to ' + self.host + ' on ip ' + remote_ip

        try :
            s.send(self.message)
        except socket.error:
            print 'Send failed'
            sys.exit()
 
        reply = s.recv(4096)
       # print 'Message send successfully'
 #       while 1:

 #           try:
 #               
 #
 #           except socket.timeout:
 #               print 'Socket timeout, loop and try recv() again'
 #               time.sleep( 5.0)
 #               # traceback.print_exc()
 #               continue
 #
 #           except:
 #               traceback.print_exc()
 #               print 'Other Socket err, exit and try creating socket again'
 #               # break from loop
 #               break

        print reply
        
#        s.close()

    def connectToServer_1(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
            sys.exit();
 
        print 'Socket Created'
  
        try:
            remote_ip = socket.gethostbyname( self.host )
 
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
     
        #print 'Ip address of ' + self.host + ' is ' + remote_ip
 
        s.connect((remote_ip , self.port))
 
        print 'Socket Connected to ' + self.host + ' on ip ' + remote_ip
        
        try :
            s.send(self.message_1)
        except socket.error:
            print 'Send failed'
            sys.exit()
 
       # print 'Message send successfully'

        reply = s.recv(4096)
        
        print reply
        
        s.close()



cc = ClientConnection()
cc.connectToServer()
cc.connectToServer_1()
