import os
import time
import pwd
import signal
import sys
import re



class ParentMethod(object):
    def __init__(self):

    
    def signal_term_handler(self, signal, frame):
        
        
        chld_pid_1 = childlist[0]
        chld_pid_2 = childlist[1]
        
        print 'got SIGTERM'
        
        chck_proc_1 = os.kill(chld_pid_1, 0)

        chck_proc_2 = os.kill(chld_pid_2, 0)

        print chck_proc_1
        print chck_proc_2


        if chck_proc_1 == None:
            print "Waiting for first child..."
            os.wait()
        elif chck_proc_2 == None:
            print "Waiting for second child..."
            os.wait()

        print chld_pid_1
        print "============"
        print chld_pid_2

        
 
    def firstChildAct(self):
        

        cur_pid = os.getpid()
        f = file("/tmp/tmp.pid", "w+")
        f.write("This childs pid is %d" % (cur_pid))
        f.seek(0)
        pr = f.read()
        f.close()
        
    def secondChildAct(self):
        
        pth = "/media/sf_CentOS/python_stud/"

    
        for file in os.listdir(pth):
            print file
        
        #time.sleep(50)
    
    def forkIt(self):
        
        global childlist
        childlist = []
        cur_pid = os.getpid()

        for i in range(0,2):
            pid = os.fork()

            if pid > 0:
                p_pid = os.getpid()
                print "I'm parent(%d) and my child is: %s" % (p_pid, pid)
                
                childlist.append(pid)
           
            else:
                if i == 0:
                    self.firstChildAct()
                else:
                    self.secondChildAct()


                #c_pid = os.getpid()
                #print "I'm %d child with pid: %d" % (i, c_pid)

                #break;




pr = PrintPr()

pr.forkIt()



signal.signal(signal.SIGTERM, pr.signal_term_handler)

    
time.sleep(10)
