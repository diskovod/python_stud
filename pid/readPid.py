import os
import re
import errno
from color import *
import time
from lockFile import *

cl = getColor()
lf_cl = FileLock()

class readingPid(object):
    def __init__(self):
        pass

    def readPid(self):
        while True:
            wp_f = os.path.dirname(os.path.realpath(__file__))
            reg_get_pid = "[\d]+"
                #reg_get_path = "(.+?)(\.[^.]*$|$)"

            wp_f = open(str(wp_f) + "/"+"myscript.pid", "r+")
	    
            wp_f.seek(0)
            r = wp_f.read()
            found_pid = re.findall(reg_get_pid, r)
            results = map(int, found_pid)
            last = str(results).strip("[]")
	    

            try:
                check_pid = os.kill(int(last), 0)
		lf_cl.lock_file(wp_f)
            except OSError as err: 
                if err.errno == 3:			
                    print cl.redText("Script is dead!!")
                    break

            print cl.greenText("Script is working!")
            wp_f.close()
            time.sleep(5)	
                #print cl.greenText("Script is working!")


wr = readingPid()
wr.readPid()
