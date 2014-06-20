#!/usr/bin/python

import socket
import sys
import traceback

class ClientConnection(object):
    def __init__(self):
        self.host = 'www.pythonstud.com'
        self.port = 80
       
    
    def getRemoteIp(self):

        try:
         
            remote_ip = socket.gethostbyname( self.host )
            
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        
        return remote_ip

    def socketConnect(self, socket, remote_ip):

        return socket.connect((remote_ip, self.port))
    
    def http_get(self, socket, request, host):
        
        try :
            socket.send("GET %s HTTP/1.1\nHost: %s\nConnection: keepalive\r\n\r\n" % (request, host))
        except socket.error:
            print 'Send failed'
            sys.exit()
 
        data = socket.recv(4096)
        
        return data


if __name__ == "__main__":

    cc = ClientConnection()
    
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout( 5.0)

    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit();
        
        print 'Socket Created'

        
    remote_ip = cc.getRemoteIp()

    cc.socketConnect(s,remote_ip)

    response_1 = cc.http_get(s, "/", "www.pythonstud.com")
    response_2 = cc.http_get(s, "/test.html", "www.pythonstud.com")

    print response_1
    print response_2

    s.close()
