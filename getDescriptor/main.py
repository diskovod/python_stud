import os
from getPid import *
import re


read_pid = readingPid()


class getDescriptor(object):

	def __init__(self):
		pass

	def getPidsData(self):
		pr = os.listdir('/proc/')
		pattern = "(\d+)"
		pids = re.findall(pattern, str(pr))
		
		return pids	

	def getFiles(self, pids):
			
		for pid in pids:
			#pid = read_pid.readPid()
			open_files = []
			fd_dir=os.path.join('/proc', str(pid), 'fd')
			fds = os.listdir(fd_dir)
			
			
		for file in fds:

			link=os.readlink(os.path.join(fd_dir, file))
			open_files.append(link)

		#for link in sorted(open_files.keys()):

		#	print "%s : %s" % (link, ", ".join(map(str, open_files[link])))
		return fd_dir

	def getType(self, path):
        	if(os.path.isfile(path) == True):
            		return "file"
        	elif (os.path.isdir(path) == True):
            		return "dir"
        	elif (os.path.islink(path) == True):
            		return "link"
        	return "unkn"

	def getPath(self, files):
	
		print files	
		fin = {}
		l_len = len(files)
		print l_len
		i = 0
		for items in files:

			fin.update({files[i]: self.getType(files[i])})
			i += 1
		print fin		

	def getListType(self, files):
		fin = [] 
		for f in files:
			type = self.getType(f)
			if type == 'file':
				fin.append(f)
		print fin	
		

cl = getDescriptor()
#f = cl.getFiles()
p = cl.getPidsData()

cl.getFiles(p)

#cl.getProcData()




