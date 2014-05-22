from lockFile import *
import time


lf = FileLock()

def sendText():
     
	fp = open("/media/sf_CentOS/python_stud/tmpfile", 'w')
	lf.lock_file(fp)
	fp.write("lolololololol")
	fp.seek(0)
	#lf.lock_file(fp)
	time.sleep(10)
	fp.close()

sendText()                   
