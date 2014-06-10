import httplib, urllib


#params = {'first_param' : 1, 'second_param' : 2, 'third_param' : 3}
#params = urllib.urlencode(params)
#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
#
#conn = httplib.HTTPConnection("google.com")
#conn.request("POST", "/cgi-bin/query", params, headers)
#response = conn.getresponse()
#data = response.read()
#print data
#conn.close()


#import httplib

conn = httplib.HTTPConnection("www.1hozain.ru")
conn.request("GET", "/index.php")
response = conn.getresponse()
data = response.read()
print data
conn.close()
