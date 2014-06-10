#!/usr/local/bin/python

import httplib



conn = httplib.HTTPConnection("www.1hozain.ru")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
h = r1.getheaders()

print h

#data1 = r1.read()
#conn.request("GET", "/parrot.spam")
#r2 = conn.getresponse()
#print r2.status, r2.reason
#
#data2 = r2.read()


conn.close()
