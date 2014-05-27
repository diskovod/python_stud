import os
from getPid import *
import re


read_pid = readingPid()


class getDescriptor(object):

	def __init__(self):
		pass

	
        def getType(self, path):
                if(os.path.isfile(path) == True):
                        return "file"
                elif (os.path.isdir(path) == True):
                        return "dir"
                elif (os.path.islink(path) == True):
                        return "link"
                return "unkn"


	def getPidsData(self):
		pr = os.listdir('/proc/')
		pattern = "(\d+)"
		pids = re.findall(pattern, str(pr))

		return pids	

        def getFileType(self, fd):
                        type = self.getType(fd)
                        if type == 'file':
                                return fd
			else:
				return ""
	def getFiles(self, pids):
			
		open_files = {}

		for pid in sorted(pids):
				
			fd_dir=os.path.join('/proc', pid, 'fd')
                	fds = os.listdir(fd_dir)
	
			for file in fds:
				try:
					link=os.readlink(os.path.join(fd_dir, file))
					files_only = self.getFileType(link)
					
						#print type(files_only)
					if files_only != "":	
						#int(pid)
						open_files.setdefault(link, []).append(pid)	
						open_files[pid] = files_only
						#open_files.update({pid: files_only})
						
				except OSError:
					continue
					
		for link in sorted(open_files.keys()):
			print "%s : %s" % (link, "".join(map(str, open_files[link])))
				
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

				

cl = getDescriptor()
#f = cl.getFiles()
p = cl.getPidsData()

cl.getFiles(p)

#cl.getProcData()




