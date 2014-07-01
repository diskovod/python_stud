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

    def getIp(self):

        return socket.gethostbyname(self.host)

    def getSubnetMask(self):
        
        return socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM),35099, struct.pack('256s', self.iface))[20:24])

    def ipToBin(self, ip):
        
        converted_ip = socket.inet_aton(ip)

        unpacked_ip = struct.unpack('!L', converted_ip)

        return unpacked_ip[0]

    def getStructedSubAddress(self, unpacked_hostip, unpacked_subnetip):

        return unpacked_hostip & unpacked_subnetip

    def BinToIp(self, structedSubAddress):

        packed_subaddr = struct.pack('!L', structedSubAddress)

        standart_string = socket.inet_ntoa(packed_subaddr)

        return standart_string

    def inverseIp(self, high_addr, subnet_mask, subnet_addr):

        inverted_mask = xor(subnet_mask, high_addr)

        broadcast_ip = xor(subnet_addr, inverted_mask)
        
        return broadcast_ip
   
    def parser(self):
        
        parser = optparse.OptionParser(version='0.01', description='Ip parser')
        parser.add_option('--ip', type='string', action = "store", dest='ip', help='Input ip')

        options,arguments=parser.parse_args()
        
        for key,value in options.__dict__.items():
            if(key == 'ip'):
                ip = value
        
        return ip

    def getValuesFromParse(self, ip):

        pattern = '^([\d]*.[\d]*.[\d]*.[\d]*).([\d])'
        result = re.search(pattern, ip)

        return result.group

    def getSubnet(self, node):
        
        if 8 <= node < 16:
            nclass = 2
        elif 16 <= node < 24:
            nclass = 3
        elif 24 <= node:
            nclass = 4

        if nclass == 2:
            subnet = "255.0.0.0"
        elif nclass == 3:
            subnet = "255.255.0.0"
        elif nclass == 4:
            subnet = "255.255.255.0"

        return subnet

#
#    def getValuesFromParse(self, parsed_ip):
#
#        ip, mask = parsed_ip.split('/')
#        octets = ip.split('.')
#        addr = 0
#        for octet in octets:
#            addr = addr * 256 + int(octet)
#
#        return addr

sa = SubAddress()


parsed_ip = sa.parser()
getval_ip = sa.getValuesFromParse(parsed_ip)

local_ip = getval_ip(1)
node = getval_ip(2)

print getval_ip(2)

subnet = sa.getSubnet(getval_ip(2))

print subnet

time.sleep(5)

#local_ip = sa.getIp()

#subnet = sa.getSubnetMask()
unpacked_ip = sa.ipToBin(local_ip)

unpacked_subnet = sa.ipToBin(subnet)

high_addr = sa.ipToBin("255.255.255.255")

structedSubAddress = sa.getStructedSubAddress(unpacked_ip, unpacked_subnet)

packedNetAddressIp = sa.BinToIp(structedSubAddress)

broadcast_ip = sa.inverseIp(high_addr, unpacked_subnet, structedSubAddress)

final_broadcast_ip = sa.BinToIp(broadcast_ip)



print "Local ip: %s" % (local_ip)
print "Subnet ip: %s" % (subnet)
#rint "Unpacked local ip: %s" % (unpacked_ip)

#print "Unpacked subnet ip: %s" % (unpacked_subnet)
#print "Bitwise result: %s" % (structedSubAddress)
print "SubNet Address: %s" % (packedNetAddressIp)

print "Broadcast ip: %s" % (final_broadcast_ip)





