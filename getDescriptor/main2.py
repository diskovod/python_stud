import os
import re

class DirectoryScanner(object):
	def __init__(self, pattern, handler):		
		self.pattern_ = pattern
		self.handler_ = handler
				
	def scan(self, path):
		pr = os.listdir(path)		
		result = re.findall(self.pattern_, str(pr))
		
		for item in result:			
			self.handler_.handle(path, item);

class ScannerHandler(object):
	def __init__(self):
		pass
	def handle(self, path, item):
		pass
		

class PidHandler(ScannerHandler):
	def __init__(self, reader):
		super(ScannerHandler, self).__init__()
		self.reader_ = reader
	
	def handle(self, path, item):
		pidinfo = self.reader_.read(path, int(item))
		if pidinfo.files_in_use:			
		   print (("PID(%s) : \n\t%s\n") % (pidinfo.pidid, '\n\t'.join(pidinfo.files_in_use)))
		
class PidInfo(object):
	def __init__(self, pidid):
		self.pidid = pidid
		self.files_in_use = []

class PidFDHandler(ScannerHandler):
	def __init__(self, pidinfo):
		super(ScannerHandler, self).__init__()
		self.pidinfo = pidinfo
		
	def handle(self, path, item):
		try:
			fpath = os.path.join(path, item)
			if os.path.islink(fpath) == True:
				realpath = os.readlink(fpath)
				if os.path.isfile(fpath) == True:
					self.pidinfo.files_in_use.append(realpath)
			else:
				pass
		except OSError:
			pass
					
class PidInfoReader(object):
	def __init__(self):
		pass
		
	def read(self, path, pid):
		pidinfo = PidInfo(pid)
		handler = PidFDHandler(pidinfo)
		scanner = DirectoryScanner("(\d+)", handler)
		scanner.scan(os.path.join(path, str(pid), 'fd'))		
		
		return pidinfo
	
if __name__ == '__main__':
	pidinforeader = PidInfoReader()
	handler = PidHandler(pidinforeader)	
	scanner = DirectoryScanner("(\d+)", handler)
	scanner.scan('/proc/')
	
