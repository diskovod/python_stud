import os
from getPid import *


read_pid = readingPid()


class getDescriptor(object):

	def __init__(self):
		pass

	
	def getFiles(self):
		
		pid = read_pid.readPid()
		open_files = []
		fd_dir=os.path.join('/proc', str(pid), 'fd')
		fds = os.listdir(fd_dir)

		for file in fds:

			link=os.readlink(os.path.join(fd_dir, file))
			open_files.append(link)

		#for link in sorted(open_files.keys()):

		#	print "%s : %s" % (link, ", ".join(map(str, open_files[link])))
		print open_files


cl = getDescriptor()
cl.getFiles()




