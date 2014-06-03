import os
import time
import pwd
import signal
import sys
import re
import datetime


class Child(object):
    def __init__(self):
        self.pid = 0
        self.terminate = False
        self.alive = False
   
    def IsAlive(self):
        print "Is alive :" + str(self.pid) + " = " + str(self.alive)
        return self.alive

    def Terminate(self, signal, frame):
        print "Termination: %d" % (self.pid)
        self.terminate = True

    def setPid(self, pid):
        self.pid = pid

    def Run(self):
        self.alive = True
        #print self.terminate
        print "I'm child: %d: id %i " % (self.pid, id(self))
        time.sleep(5)
        #elf.alive = False


class Parent(object):
    def __init__(self):
        self.childlist = []
        self.termProc = False

    def TerminateAll(self):
        print self.childlist
        if self.termProc == True:
            for child in self.childlist:
                isWork = os.kill(child, 0)
                if isWork == None:
                    print "Terminate child with id: %i" % (child)
                    #os.waitpid(child, 0)
                    os.kill(child, signal.SIGTERM)
                    time.sleep(5)
                    self.childlist.pop(0)
            else:
               pass
        print self.childlist           

    def signal_term_handler(self, signal, frame):
        
        self.termProc = True
        print 'got SIGTERM'
        self.TerminateAll()
        print self.childlist
            
    def CreateChild(self):
        child = Child()
        cur_pid = os.getpid()

        pid = os.fork()
        #pid = 1
        if pid > 0:
            print "Child created: %s : id %i" % (pid, id(child))
            self.childlist.append(pid)
        else:
            print "Par pid %d" % (cur_pid)
            print "In child id %i" % (id(child))
            child.setPid(os.getpid())
            child.Run()

pr = Parent()

print "1: CreateChild"
pr.CreateChild()
print "2: CreateChild"
pr.CreateChild()
print "3: CreateChild"

signal.signal(signal.SIGTERM, pr.signal_term_handler)
time.sleep(50)
#pr.TerminateAll()
