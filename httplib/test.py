#!/usr/local/bin/python
import httplib, urllib, urllib2
#u = urllib.urlopen("http://pythonstud.com/")
# 
#print u.read()

#params = urllib.urlencode({'username': 'steve', 'password': '111111'})
#headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
#
#conn = httplib.HTTPConnection("www.pythonstud.com")
#conn.request("POST", "/login.php", params, headers)
#r1 = conn.getresponse()
##h = r1.read()
#
#data = r1.read()
#
#
#print r1.status, r1.reason
#
#print data

url = 'http://www.pythonstud.com/login.php'
data = urllib.urlencode({'name' : 'joe',
                         'age'  : '10'})
content = urllib2.urlopen(url=url, data=data).read()
print content

#data1 = r1.read()
#conn.request("GET", "/parrot.spam")
#r2 = conn.getresponse()
#print r2.status, r2.reason
#
#data2 = r2.read()


#conn.close()
