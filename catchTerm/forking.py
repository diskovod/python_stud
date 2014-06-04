#!/usr/local/bin/python

import os
import time
import pwd
import signal
import sys
import re
import datetime


class Child(object):
    def __init__(self):
        self.terminate = False
        self.alive = False
        signal.signal(signal.SIGTERM, self.child_signal_handler)

    def child_signal_handler(self, signal, frame):
       
        isClosed = os.kill(self.pid, 0)

        if isClosed == None:

            print "Child %d closed!" % (self.pid)
            sys.exit(0)
        
        else:

            print "Child still working..."

    def setPid(self, pid):
        self.pid = pid

    def Run(self):
        self.alive = True
        print "I'm child: %d" % (self.pid)
        time.sleep(20)
        
class Parent(object):
    def __init__(self):
        self.childlist = []
        self.termProc = False
        self.isChildTerminated = False

    def TerminateAll(self):
        if self.termProc == True:
            for child in self.childlist:
                print "Terminate child with id: %i" % (child)
                os.kill(child, signal.SIGTERM)
            else:
               pass

    def signal_term_handler(self, signal, frame):
        self.termProc = True
        print 'got SIGTERM'
        self.TerminateAll()
            
    def CreateChild(self):
        child = Child()
        cur_pid = os.getpid()

        pid = os.fork()
        if pid > 0:
            
            self.childlist.append(pid)
        
        else:
        
            print "Parent pid is: %d" % (cur_pid)
            child.setPid(os.getpid())
            child.Run()

pr = Parent()


pr.CreateChild()
pr.CreateChild()


signal.signal(signal.SIGTERM, pr.signal_term_handler)
time.sleep(40)
