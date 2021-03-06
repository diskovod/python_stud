import os
import time
import pwd
from getProcessPid import *


pid_cl = getProcPid()


class PrintPr(object):
    def __init__(self):
        pass
    
    def printIt(self):
        
        print "This is process for test"
        time.sleep(30)
    
    def getUsrByName(self, name):
        g_name = pwd.getpwnam(name)

        return g_name.pw_uid

    def forkIt(self):
        
        cur_pid = os.getpid()
        print "I'm parent: %s" % (cur_pid)

        for i in range(0,2):
            pid = os.fork()

            if pid:
            
                print "I'm child: %s" % (pid)
                chldlist.append(pid)
           
            else:
                c_pid = os.getpid()
                g_name = pwd.getpwnam("nobody")
                nby_id = g_name.pw_uid
                nby_gid = g_name.pw_gid

                set_gid = os.setgid(nby_gid)
                set_uid = os.seteuid(nby_id)
                
                pid_cl.createPidFile(c_pid)
                #time.sleep(50)
                break;

        for childf in childlist:
            os.kill(child, SIGKILL)
           
        #fout.write('\nEnd of file')

pr = PrintPr()

pr.forkIt()
