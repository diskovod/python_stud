from lockTmp import *
import time
import os


lf = TmpLock()

class writeToTmp(object):

	def __init__(self):
		pass

	def writeText(self):

        	fp = open("/media/sf_CentOS/python_stud/getDescriptor/tmpfile", 'w')
        	lf.tmp_lock(fp)
        	fp.write("lolololololol11")
        	fp.seek(0)
        	time.sleep(200)
        	fp.close()

   	def getPid(self):
        	wp = os.path.dirname(os.path.realpath(__file__))
        	curr_pid = os.getpid()
        	#reg_get_pid = "[\d]+"
        	#reg_get_path = "/(.*?)/$"

        	wp_f = open(str(wp) + "/"+"myscript.pid", "r+")
        	wp_f.write("Pid: %s, Working Path: %s" % (str(curr_pid), str(wp)))
        	wp_f.seek(0)
        	r = wp_f.read()
        	print r
        	wp_f.close()

tm_cl = writeToTmp()
tm_cl.getPid()
tm_cl.writeText()


