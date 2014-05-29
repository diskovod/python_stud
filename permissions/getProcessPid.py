import os

class getProcPid(object):
    def __init__(self):
        pass

    def setTmpPerm(self, f, perm):

        return os.chmod(f, perm)
   
    def writeToPidFile(self, f, pid):

        fn = "/tmp/myprocess.pid"
        #curr_pid = os.getpid()
        #wp_f = open(tmp_path + "/"+"myprocess.pid", "r+")
        f.write("Child Pid: %d" % (pid))
        f.seek(0)
        r = f.read()
        print r
        f.close()
        self.setTmpPerm(fn, 0600)

    def createPidFile(self, pid):
    
        if os.path.exists("/tmp/myprocess.pid"):
            f = file("/tmp/myprocess.pid", "r+")
        
            self.writeToPidFile(f, pid)
        #fn = "/tmp/myprocess.pid"
        #curr_pid = os.getpid()
        #wp_f = open(tmp_path + "/"+"myprocess.pid", "r+")
        #f.write("Child Pid: %d" % (pid))
        #f.seek(0)
        #r = f.read()
        #print r
        #f.close()
        #self.setTmpPerm(f, 0600)

        else:

            f = file("/tmp/myprocess.pid", "w+")

            self.writeToPidFile(f, pid)

        # tmp_path = "/tmp"
       
    
