#!/usr/local/bin/python

import pycurl
def getUserData():
	c = pycurl.Curl()
	c.setopt(pycurl.URL, 'https://api.github.com/users/diskovod')
	c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
	c.setopt(pycurl.VERBOSE, 0)
	c.setopt(pycurl.USERPWD, 'username:userpass')
	c.perform()

getUserData()
