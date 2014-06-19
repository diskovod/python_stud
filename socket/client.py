#!/usr/bin/python

import socket
import errno

class ClientSocket(object):
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "127.0.1.1"
        self.port = 80
       # self.string = "Hello world!"
      #  self.request = [
      #              "GET / HTTP/1.0",
      #              "Host: www.pythonstud.com",
      #              "Connection: Close",
      #              "\r\n"
      #              ]
        self.request = "GET / HTTP/1.0"
        self.main_host = "Host: www.pythonstud.com"
        self.CRLF = "\r\n"


    def serverConnection(self):
        try:

            self.s.connect((self.host, self.port))
            #print self.s.recv(1024)
            #self.s.send(self.CRLF.join(self.request))
            self.s.send(self.request)
            self.s.send(self.main_host)
            self.s.send(self.CRLF)
            response = ''
            buffer = self.s.recv(4096)
            while buffer:
                response += buffer
                buffer = self.s.recv(4096)

            # HTTP headers will be separated from the body by an empty line
            #header_data, _, body = response.partition(self.CRLF + self.CRLF)

            #print header_data
            data = self.s.recv(1024)
            print data


            self.s.close()

        except Exception,e:
            print "Error is %s" % (e)



cl = ClientSocket()
cl.serverConnection()
