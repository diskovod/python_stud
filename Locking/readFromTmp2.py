
from shared_locking import *
import time


lf = ShareLock()

def readText():

        fp = open("/media/sf_CentOS/python_stud/tmpfile", 'r')
        lf.sh_lock_file(fp)
        rd = fp.read()
        fp.seek(0)
        print rd
        #lf.sh_lock_file(fp)
        time.sleep(15)
        fp.close()

readText()


