#!/usr/local/bin/python

import datetime
import os
import time
from multiprocessing import Queue
from multiprocessing import Process
from Queue import Empty



#class Child(Process):
##    def __init__(self, queue):
#        super(Child, self).__init__()
#        self.queue= queue
#
#    def run(self):
#        print 'Worker started'
#        # do some initialization here
#
#        print 'Computing things!'
#

class Child (Process):
    def __init__(self, chld_name, queue):
        Process.__init__(self)
        self.queue = queue
        self.chld_name = chld_name
        
    def run(self):
        print "Starting " + self.name
        
        pid = os.getpid()
        print pid
        while self.queue:
            try:
                q = self.queue.get_nowait()
                print '%s: have: %s' % (self.chld_name, q)
                
            except Empty, e:

                print '%s: Empty' % (self.chld_name)

            time.sleep(2)


class Parent(object):
    def __init__(self):
        self.q = Queue()
        self.child_1 = Child("Child-1", self.q)
        self.child_2 = Child("Child-2", self.q)

    def writeToQueue(self):
        
        while True:
            
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            self.q.put(st)

            time.sleep(1)


    def CreateChild(self):
       # child = Child(self.q)
         
        self.child_1.start()
        self.child_2.start()



pr = Parent()

pr.CreateChild()
pr.writeToQueue()


    
    

        
#pr.writeToQueue()
