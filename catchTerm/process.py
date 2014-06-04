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
        
    def handle_term(self, signal, frame):
        
        print "Childs"


   # def IsAlive(self):
   #     print "Is alive :" + str(self.pid) + " = " + str(self.alive)
   #     return self.alive

    def setPid(self, pid):
        print "get pid %s" % (pid)

        self.pid = pid


    def Terminate(self):
        print "Termination: %s" % (self.pid)
        self.terminate = True

    def Run(self):
       # self.alive = True
       # while not self.terminate:
        print "I'm child: %s: " % (self.pid)
        time.sleep(15)
        self.alive = False

class Parent(object):
    def __init__(self):
        self.childlist = []

    def TerminateAll(self):
        
        #print self.childlist
        for child in self.childlist:
            print "Terminate child with id: %i" % (child.pid)
            child.Terminate()
            #os.waitpid(child.pid, 0)
    
    def signal_term_handler(self, signal, frame):
        
        print 'got SIGTERM'

        print self.childlist
            
    def CreateChild(self):
        child = Child()
        cur_pid = os.getpid()

        pid = os.fork()

        if pid > 0:
            print "Child created: %s : id %i" % (pid, id(child))

            self.childlist.append(child)
        else:
            print "In child id %i" % (id(child))
            child.setPid(os.getpid())
            child.Run()

pr = Parent()

pr.CreateChild()
pr.CreateChild()

time.sleep(10)
pr.TerminateAll()

signal.signal(signal.SIGTERM, pr.signal_term_handler)
