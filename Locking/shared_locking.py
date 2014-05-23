
import warnings
import fcntl

class ShareLock(object):
        def __init__(self):
                pass


        def sh_lock_file(self, file):
                #print file
                #file = open("/media/sf_CentOS/python_stud/myscript.pid", "w")
                print file.fileno()
                try:
                        fcntl.flock(file.fileno(), fcntl.LOCK_SH|fcntl.LOCK_NB)
                        print "Shared Locking!"
                except IOError:
                        warnings.warn("Shared locking detected ($!), blocking ...")
                        fcntl.flock(file.fileno(), fcntl.LOCK_SH)


