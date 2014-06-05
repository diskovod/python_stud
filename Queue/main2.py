#!/usr/local/bin/python

import datetime
import os
import time
from multiprocessing import Queue
from multiprocessing import Process
from Queue import Empty
import signal
import sys



class Child(object):
    def __init__(self, queue):
        #self.pid = os.getpid()
        self.queue = queue
        
    def setPid(self, pid):
        self.pid = pid

    def child_signal_handler(self, signal, frame):
       
        isClosed = os.kill(self.pid, 0)

        if isClosed == None:

            print "Child %d closed!" % (self.pid)
            sys.exit(0)
        
        else:

            print "Child still working..."    

    def Run(self):
        
        signal.signal(signal.SIGTERM, self.child_signal_handler)
        self.pid = os.getpid()
        while self.queue:
            try:
                q = self.queue.get()
                print 'I found something new my id: %s' % (self.pid)
                print q
            except Empty, e:
                print 'Found nothing in the queue'
                
            time.sleep(1)


class Parent(object):
    def __init__(self):
        self.q = Queue()
        self.childlist = []

    def writeToQueue(self):
        
        while True:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            self.q.put(st)
             
            time.sleep(1)
    
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
        child = Child(self.q)
        cur_pid = os.getpid()

        pid = os.fork()
        if pid > 0:
            
            print "I'm parent with id: %s" % (cur_pid)
            print "My child is: %s" % (pid)
            self.childlist.append(pid)
        
        else:
        
            child.Run()

pr = Parent()

signal.signal(signal.SIGTERM, pr.signal_term_handler)

pr.CreateChild()
pr.CreateChild()



pr.writeToQueue()


