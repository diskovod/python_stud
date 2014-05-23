
import warnings
import fcntl

class FileLock(object):
	def __init__(self):
		pass


	def lock_file(self, file):
		#print file
		#file = open("/media/sf_CentOS/python_stud/myscript.pid", "w")
		print file.fileno()		
		try:
    			fcntl.flock(file.fileno(), fcntl.LOCK_EX)
			print "Locked!"
		except IOError:
    			warnings.warn("can't immediately write-lock the file ($!), blocking ...")
    			fcntl.flock(file.fileno(), fcntl.LOCK_EX)


#l_cl = FileLock()
#l_cl.lock_file()

