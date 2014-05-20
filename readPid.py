import os
import re
import errno
from color import *
import time

cl = getColor()

class readingPid(object):
	def __init__(self):
		pass
	
	def readPid(self):
		while True:
			try:
				wp_f = os.path.dirname(os.path.realpath(__file__))
				reg_get_pid = "[\d]+"
        			#reg_get_path = "(.+?)(\.[^.]*$|$)"

				wp_f = open(str(wp_f) + "/"+"myscript.pid", "r+")
        			wp_f.seek(0)
        			r = wp_f.read()
				found_pid = re.findall(reg_get_pid, r)
				results = map(int, found_pid)
				last = str(results).strip("[]")
				check_pid = os.kill(int(last), 0)
				print cl.greenText("Script is working!")
				time.sleep(5)	
        			wp_f.close()
				#print cl.greenText("Script is working!")
					
			except OSError as err: 
                		if err.errno == 3:
					
					#print cl.redText("Script is dead!!")
					count = 1
					break
		else: 
			if count == 1:
				print cl.redText("Script is dead!!")
wr = readingPid()
wr.readPid()
