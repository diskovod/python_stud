import json
import tempfile
import commands
import os

class tempData(object):
	def __init__(self):
		pass
	def writeToTmpFile(self, info):
		for filename in os.listdir("/media/sf_CentOS/"):
            		if filename.startswith('tmpParseData'):
                		os.remove(filename) 

        	dirname, basename = os.path.split('tmpParseData')
        	f = tempfile.NamedTemporaryFile(prefix=basename, dir=dirname, delete=False)

        	data = """%s""" % (info)  
	#	print type(info)
        	json.dump(data, f)
        	f.flush()
        	f.seek(0)
		print f.name
        	#print(json.load(f))
