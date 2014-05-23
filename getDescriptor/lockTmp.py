import warnings
import fcntl

class TmpLock(object):
        def __init__(self):
                pass


        def tmp_lock(self, file):
                try:
                        fcntl.flock(file.fileno(), fcntl.LOCK_EX)
                        print "Locked!"
                except IOError:
                        warnings.warn("can't immediately write-lock the file ($!), blocking ...")
                        fcntl.flock(file.fileno(), fcntl.LOCK_EX)


