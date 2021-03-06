#!/usr/bin/env python


import socket
import struct
import sys
import fcntl



class SubAddress(object):
    def __init__(self):
        self.iface = "lo"

    
    def getHostName(self):

        return socket.gethostname()

    def getIp(self, hostname):
        
        return socket.gethostbyname(hostname)

    def getSubnetMask(self):
        
        return socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM),35099, struct.pack('256s', self.iface))[20:24])

#    def unpackIp(self, ip):
#
#       return struct.unpack('L',socket.inet_aton(str(ip)))[0]

    def convertHostIp(self, ip):

        return socket.inet_aton(ip)

    def convertMaskAddress(self, subnet):

        return socket.inet_aton(subnet)

    def unpackHostIp(self, converted_ip):

        return struct.unpack('!L', converted_ip)

    def unpackSubnet(self, converted_subnet):

        return struct.unpack('!L', converted_subnet)


    def getStructedAddress(self, unpacked_ip, unpacked_subnet):

        return unpacked_ip[0] & unpacked_subnet[0]

    def packNetAddressIp(self, subAddress):

        return struct.pack('!L', subAddress)

    def unconvertResult(self, finalsubAddress):
        
        return socket.inet_ntoa(finalsubAddress)




sa = SubAddress()

hostname = sa.getHostName()

local_ip = sa.getIp(hostname)

subnet = sa.getSubnetMask()

converted_ip = sa.convertHostIp(local_ip)

converted_subnet = sa.convertMaskAddress(subnet)

unpacked_ip = sa.unpackHostIp(converted_ip)

unpacked_subnet = sa.unpackSubnet(converted_subnet)

structedAddress = sa.getStructedAddress(unpacked_ip, unpacked_subnet)

packedNetAddressIp = sa.packNetAddressIp(structedAddress)

final_result = sa.unconvertResult(packedNetAddressIp)



print "Your local ip: %s" % (local_ip)

print "Your Subnet Mask: %s" % (subnet)

print "Unpacked ip: %s" % (unpacked_ip)

print "Unpacked Mask Address: %s" % (unpacked_subnet)

print "Structed Subnetwork Address: %s " % (structedAddress)

print "Subnetwork address is: %s" % (final_result)
