#!/usr/bin/env python

import optparse, os
import socket
import struct
import sys
import fcntl
import time
from operator import xor
import re
import select
import socket


class LiveServer(object):
    def __init__(self, server):
        self.host = ''
        self.port = 8000
        self.sub_addr = '10.0.2.0'
        self.sub_mask = '255.255.255.0'
        self.backlog = 5 
        self.size = 1024
        self.server = server
        self.server_list = [server]
        self.client_dict = {}
        self.client_data = {}
        self.message_conn = "Client connected:"
        self.message_disc = "Client disconnected:"


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
            
            print "%s %s" % (self.message_conn ,str(address))

            self.client_dict.update({client: address})

    def main(self):
        
        try:
            while True:

                inputready,outputready,exceptready = select.select(self.server_list,self.server_list,self.server_list, 0)
                self.client_connect(inputready)
        
        except KeyboardInterrupt:
            print "Programm closed"



try:

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error, e:

    print "Error is %s" % (e)


ls = LiveServer(server)

ls.bindServer()
ls.listenServer()
ls.main()




