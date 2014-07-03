#!/usr/bin/env python

import optparse, os
import socket
import struct
import sys
import fcntl
import time
from operator import xor
import re


class SubAddress(object):
    def __init__(self):
        self.iface = "lo"
        self.host = socket.gethostname()
        self.action = ''
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

    def getStructedSubAddress(self, unpacked_hostip, unpacked_subnetip):

        return unpacked_hostip & unpacked_subnetip

    def BinToIp(self, structedSubAddress):
        try:
            packed_subaddr = struct.pack('!L', structedSubAddress)
        except struct.error, err:
            print 'Exception error is: %s' % err
        except TypeError, terr:
            print 'Exception error is: %s' % terr
        try:
            standart_string = socket.inet_ntoa(packed_subaddr)
        except socket.error, e:
            print 'Exception error is: %s' % e
 
        return standart_string

    def inverseIp(self, high_addr, subnet_mask, subnet_addr):

        inverted_mask = xor(subnet_mask, high_addr)
        broadcast_ip = xor(subnet_addr, inverted_mask)
        return broadcast_ip
   
    def parser(self):
        try:
            parser = optparse.OptionParser(version='0.01', description='Ip parser')
            parser.add_option('--ip', type='string', action = "store", dest='ip', help='Input ip')
            #parser.add_option('--sip', type='string', action = "store", dest='sip', help='Input subnet ip and mask')
            options,arguments=parser.parse_args()
            
           # print options.__dict__.items()[0]
            for key,value in options.__dict__.items():
                if(key == 'ip'):
                    ip = value

        except OSError as e:
            print 'Exception error is: %s' % e
        
        return ip

#    def checkAction(self):
#        if self.action == 0:
#            return 0
#        elif self.action == 1:
#            return 1

    def getValuesFromParse(self, ip):

        pattern = '^([\d]*.[\d]*.[\d]*.[\d]*).([\d]*)'
        result = re.search(pattern, ip)

        return result.group

    def getSubnet(self, node, high_address):
        
        shift_num = 32 - node
        right_shift = high_address >> shift_num
        subnet = right_shift << shift_num

        return subnet

    def checkIpinSubnet(self, ip, sub_addr, sub_mask):
        
        if(sub_addr == (ip & sub_mask)):
            return "True"
        else:
            return "False"

sa = SubAddress()

high_address = "255.255.255.255"
parsed_ip = sa.parser()

splitted = parsed_ip.split("/")

host_ip = splitted[0]
subnet_ip = splitted[1]
subnet_mask = ''

getval_ip = sa.getValuesFromParse(parsed_ip)

    
local_ip = getval_ip(1)
node = getval_ip(2)

if subnet_mask:

    unpacked_host_ip = sa.ipToBin(host_ip)
    unpacked_subnet_ip = sa.ipToBin(subnet_ip)
    unpacked_subnet_mask = sa.ipToBin(subnet_mask)
    
    result = sa.checkIpinSubnet(unpacked_host_ip, unpacked_subnet_ip, unpacked_subnet_mask)

    print result
    
else:


    high_addr = sa.ipToBin(high_address)

    unpacked_subnet = sa.getSubnet(int(getval_ip(2)), high_addr)
    subnet = sa.BinToIp(unpacked_subnet)

    unpacked_ip = sa.ipToBin(local_ip)

    structedSubAddress = sa.getStructedSubAddress(unpacked_ip, unpacked_subnet)

    packedNetAddressIp = sa.BinToIp(structedSubAddress)

    broadcast_ip = sa.inverseIp(high_addr, unpacked_subnet, structedSubAddress)

    final_broadcast_ip = sa.BinToIp(broadcast_ip)

    print "Local ip: %s" % (local_ip)
    print "Subnet mask: %s" % (subnet)
    print "SubNet Address: %s" % (packedNetAddressIp)
    print "Broadcast ip: %s" % (final_broadcast_ip)
