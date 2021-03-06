#!/usr/local/bin/python

import datetime
import os
import time
from multiprocessing import Queue
from multiprocessing import Process
from Queue import Empty
import signal
import sys
import threading


class Child (Process):
    def __init__(self, chld_name, queue):
        Process.__init__(self)
        self.queue = queue
        self.chld_name = chld_name
        self.event = threading.Event()

    def child_signal_handler(self, signal, frame):
        
        self.event.set()
        pid = os.getpid()
        
        isClosed = os.kill(pid, 0)

        if isClosed == None:

            print "Child %s with pid: %d closed!" % (self.chld_name, pid)
            self.event.clear()
            sys.exit(0)
        
        else:

            print "Child still working..."    
    
        

    def run(self):

        signal.signal(signal.SIGTERM, self.child_signal_handler)

        print "Starting " + self.name
        
        while not self.event.is_set():
            #while self.queue:
            try:
                q = self.queue.get()
                print '%s: have: %s' % (self.chld_name, q)
                
            except Empty, e:

                print '%s: Empty' % (self.chld_name)

            time.sleep(2)
            #self.event.wait()

class Parent(object):
    def __init__(self):
        self.q = Queue()
        self.child_1 = Child("Child-1", self.q)
        self.child_2 = Child("Child-2", self.q)
        signal.signal(signal.SIGTERM, self.signal_term_handler)
        self.cur_pid = os.getpid()

    def writeToQueue(self):
        
        while True:
            
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            self.q.put(st)

            time.sleep(1)

    def TerminateAll(self):

        if self.termProc == True:

            #for child in self.childlist:
            print "Terminate child: %s" % (self.child_1.name)
            self.child_1.terminate()

            print "Terminate child: %s" % (self.child_2.name)
            self.child_2.terminate()
            sys.exit(0)
            #os.kill(l)

        else:
            pass

    def signal_term_handler(self, signal, frame):

        self.termProc = True
        print 'got SIGTERM, Event started'
        self.TerminateAll()

    def CreateChild(self):
        
        
        print "Parent pid is: %s" % (self.cur_pid)
         
        self.child_1.start()
        self.child_2.start()



pr = Parent()

pr.CreateChild()
pr.writeToQueue()


    
    

        
#pr.writeToQueue()
