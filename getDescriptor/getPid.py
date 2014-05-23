import os
import re



class readingPid(object):
    def __init__(self):
        pass

    def readPid(self):

            wp_f = os.path.dirname(os.path.realpath(__file__))
            reg_get_pid = "[\d]+"
                #reg_get_path = "(.+?)(\.[^.]*$|$)"

            wp_f = open(str(wp_f) + "/"+"myscript.pid", "r+")

            wp_f.seek(0)
            r = wp_f.read()
            found_pid = re.findall(reg_get_pid, r)
            results = map(int, found_pid)
            last = str(results).strip("[]")
	    return last


#cl = readingPid()
#cl.readPid()


