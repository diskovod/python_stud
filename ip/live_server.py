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
        self.sub_list = ["10.0.2.0/255.255.255.0", "10.23.23.0/255.0.0.0"]
        #self.sub_addr = '10.0.2.0'
        #self.sub_mask = '255.255.255.0'
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

    def ipToBin(self, ip):

        try:
            converted_ip = socket.inet_aton(ip)
        except socket.error, e:
            print 'Exception error is: %s' % e
        try:
            unpacked_ip = struct.unpack('!L', converted_ip)
        except struct.error, err:
            print 'Exception error is: %s' % err
        return unpacked_ip[0]

    def checkIpinSubnet(self, ip, sub_addr, sub_mask):
        
        if(sub_addr == (ip & sub_mask)):
            return "True"
        else:
            return "False"

    def client_connect(self, inputready):
        
        for s in inputready:

            client, address = self.server.accept()
            
            self.client_dict.update({client: address})
    
    def getSubValues(self):
        
       # for item in self.sub_list:
       #     (left, right) = item.split('/');
       #     print left, right, "\n"

           # for sub in self.sub_list:
           #     for key in sub:
                    #sub[key] = int(sub[key])
           #         print key

        sublist = ["10.0.2.0/255.255.255.0", "10.23.23.0/255.0.0.0"]
        targets = ["10.0.2.255", "10.1.0.4", "192.168.1.1"]
        for target in targets:
            valid = False
            targetparts = target.split('.')
            for item in sublist:
                (ip, mask) = item.split('/');
                iptobin
                ipparts = ip.split('.')
                maskparts = mask.split('.')
                valid = True
                for i in range(4):
                    if maskparts[i] == 0:
                        break
                    if (int(targetparts[i])& int(maskparts[i])) != (int(ipparts[i])  & int(maskparts[i])):
                        valid = False
                        break
                if  valid:
                    break
            print target + " = " + str(valid) + "\n"


    #def checkIp(self, unpacked_host_ip, unpacked_subnet_ip, unpacked_subnet_mask):
        

        
    def main(self):
        
        try:
            self.getSubValues()
            
            while True:

                inputready,outputready,exceptready = select.select(self.server_list,self.server_list,self.server_list, 0)
                #self.checkIp(inputready)
                #self.checkIp(inputready)
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




