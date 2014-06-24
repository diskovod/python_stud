#!/usr/bin/env python 

import select
import socket
import sys
import time
import logging


class Server(object):
    def __init__(self, server):
        self.host = ''
        self.port = 8000 
        self.backlog = 5 
        self.size = 1024
        self.server = server
        self.server_list = [server]
        self.client_dict = {}
        self.client_data = {}

    def bindServer(self):

        try:

            return self.server.bind((self.host,self.port))

        except socket.error, e:

            print "Error is %s" % (e)
            sys.exit()

    def listenServer(self):
        self.server.listen(self.backlog)

    def client_connect(self, inputready):
        
        for s in inputready:

            client, address = self.server.accept()
            
            print "Client connected: %s" % (str(address))

            self.client_logging(1, str(address))
            self.client_dict.update({client: address})
            self.client_data[client] = '' 
            print self.client_data
             

    def client_read(self, readready):
        
        for s in readready:
            #socket = self.client_dict
            data = s.recv(self.size)
            if data:
                print data
                self.client_data[s] = data
            else:

                s.close()
                print "Client disconnected: %s" % (str(self.client_dict[s]))
                self.client_logging(0,str(self.client_dict[s]))
                del self.client_dict[s]
                del self.client_data[s]
                

    def client_write(self, writeready):
       

        for s in writeready:

            if self.client_data[s]:
     
                s.send(self.client_data[s])
                self.client_data[s] = ''

    def client_logging(self, status, address):

        logger = logging.getLogger('myapp')
        hdlr = logging.FileHandler('/var/log/pythoninfo.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)

        if status == 0:
            logger.info("Client disconnected: %s" % (address))
        elif status == 1:
            logger.info("Client connected: %s" % (address))
        else:
            logger.info("Unknown error!!!")

                
    def main(self):

        try:
            while True:

                inputready,outputready,exceptready = select.select(self.server_list,self.server_list,self.server_list, 0)
                self.client_connect(inputready)

                readready, writeready, exceptread = select.select(self.client_dict,self.client_dict,self.client_dict, 0)
                self.client_read(readready)

                readready, writeready, exceptread = select.select(self.client_dict,self.client_dict,self.client_dict, 0)
                self.client_write(writeready)
                time.sleep(0.1)
        
            self.server.close()
        except KeyboardInterrupt:
            print "Programm closed"


try:

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error, e:

    print "Error is %s" % (e)
 

s = Server(server)

s.bindServer()
s.listenServer()
s.main()



