import os
import time


class PrintPr(object):
    #def __init__(self):
    #    pass
    
    def printIt(self):
        
        print "This is process for test"
        time.sleep(30)

    def forkIt(self):
        
        cur_pid = os.getpid()
        pid = os.fork()
        print "Parent pid: %s; Child pid: %s" % (cur_pid, pid)
        #if pid > 0:
         #   fout = open('child.txt', 'w')
         #   fout.write('File created by child process %d' % pid)
        #else:
         #   fout = open('parent.txt', 'w')
         #   fout.write('File created by parent process')
        #time.sleep(100)
        #fout.write('\nEnd of file')

pr = PrintPr()
pr.forkIt()
