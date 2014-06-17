#!/usr/local/bin/python
import socket


class GetHostName(object):
    def __init__(self):
        pass

    def getName(self):

        return socket.gethostbyname('cisco.com')


gn = GetHostName()
print gn.getName()
