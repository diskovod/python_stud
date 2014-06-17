#!/usr/local/bin/python

import urllib2, base64, httplib, urllib

class BasicAuthorize(object):
    def __init__(self):
        self.url = "http://www.pythonstud.com/login.php/"
        self.username = "steve"
        self.password = "111111"

    def main(self):
 
        post_data = urllib.urlencode({"username" : self.username, "password" : self.password})
        print post_data
        req = urllib2.Request(self.url + "/?" + post_data, post_data)
        
        try:
           res = urllib2.urlopen(req)
           data = res.read()
        
        except IOError, e:

            if hasattr(e, 'reason'):
                err = "%s ERROR(%s)" % (self.url,e.reason)
                print err
            elif hasattr(e, 'code'):
                if e.code != 401:
                    err = "%s ERROR(%s)" % (self.url,e.code)
                    print err
                elif e.code == 401:
                    base64string = base64.encodestring('%s:%s' % (self.username, self.password))
                    authheader =  "Basic %s" % base64string
                    req.add_header("Authorization", authheader)
                    try:
                        
                        res = urllib2.urlopen(req)
                        data = res.read()

                        print data
                    except IOError, e:
                        if hasattr(e, 'reason'):
                            err = "%s:%s@%s ERROR(%s)" % (self.username,self.password,self.url,e.reason)
                            print err
                        elif hasattr(e, 'code'):
                            err = "%s:%s@%s ERROR(%s)" % (self.username,self.password,self.url,e.code)
                            print err
                    else:
                        err = "%s query complete" % (self.url)
                        print err

auth = BasicAuthorize()
auth.main()

