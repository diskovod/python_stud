#!/usr/bin/env python 

import select
import socket
import sys
import time

class Server(object):
    def __init__(self, server):
        self.host = ''
        self.port = 8000 
        self.backlog = 5 
        self.size = 1024
        self.server = server
        self.client_list = [server]
        self.client_dict = {}

    def bindServer(self):
        return self.server.bind((self.host,self.port))

    def listenServer(self):
        self.server.listen(self.backlog)

    def client_connect(self, inputready):
        
        for s in inputready:

            client, address = self.server.accept()
           # print "%s connected" % (address)
            print address
            self.client_list.append(client)
            

    def client_read(self, inputready):

        for s in inputready:

            data = s.recv(self.size)
            if data:
                print data
                print client_list
            else:
                s.close()
                self.client_list.remove(s)

    def main(self):

        #client_list = [self.server]
        running = 1
        while running:

            inputready,outputready,exceptready = select.select(self.client_list,self.client_list,self.client_list, 0)

        #    for s in inputready:

        #        if s == self.server:
                    # handle the server socket


            self.client_connect(inputready)
            self.client_read(inputready)
            time.sleep(0.1)
        
        self.server.close()


            

            #    elif s == sys.stdin:
                    # handle standard input 
            #        junk = sys.stdin.readline()
                   # running = 0 

           # else:
           #         # handle all other sockets 
           #         data = s.recv(self.size)
           #         if data:
           # #     s.send(data)
           #             print data
           #         else:
           #             print input
           #             s.close()
           #             input.remove(s)
           #            # running = 0
           #            # break
       
try:

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error, e:

    print "Error is %s" % (e)
 

s = Server(server)

s.bindServer()
s.listenServer()
s.main()

