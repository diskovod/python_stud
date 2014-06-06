#!/usr/local/bin/python

import datetime
import os
import time
from multiprocessing import Queue
from Queue import Empty
import signal
import sys
import threading


class Child (threading.Thread):
    def __init__(self, chld_name, queue, e):
        threading.Thread.__init__(self)
        self.queue = queue
        self.chld_name = chld_name
        self.event = e

    def child_signal_handler(self):
        
        #self.event.set()

        if self.event.is_set():
            pid = os.getpid()
        
            isClosed = os.kill(pid, 0)

            if isClosed == None:

                print "Child %s with pid: %d closed!" % (self.chld_name, pid)
                self.event.clear()
                sys.exit(0)
        
            else:

                print "Child still working..."    
    
        

    def run(self):

       # 
        print "Starting " + self.name
        
        while not self.event.is_set():
           # self.child_signal_handler()
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
        
        self.event = threading.Event()

        self.child_1 = Child("Child-1", self.q, self.event)
        self.child_2 = Child("Child-2", self.q, self.event)
        
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
            #self.child_1.quit()

            print "Terminate child: %s" % (self.child_2.name)
            #self.child_2.quit()
            sys.exit(0)
            #os.kill(l)

        else:
            pass

    def signal_term_handler(self, signal, frame):
        
        self.event.set()
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
