#!/usr/local/bin/python

import datetime
import os
import time
from multiprocessing import Queue
from multiprocessing import Process
from Queue import Empty


class Child(object):
    def __init__(self, queue):
        self.queue = queue


    def setPid(self, pid):
        self.pid = pid

    def Run(self):
        
        try:
            self.queue.get()
            print 'I found something new my id: %s' % (self.pid)
            print self.queue.get()
        except Empty, e:
            print 'Found nothing in the queue'
            


class Parent(object):
    def __init__(self):
        self.q = Queue()
        self.childlist = []

    def writeToQueue(self):
        
        while True:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            self.q.put(st)

#            print self.q.get()
             
            time.sleep(1)
           
    def CreateChild(self):
        child = Child(self.q)
        cur_pid = os.getpid()

        pid = os.fork()
        if pid > 0:
            
            print "I'm parent with id: %s" % (cur_pid)
            print "My child is: %s" % (pid)
            self.writeToQueue()
            self.childlist.append(pid)
        
        else:
        
          #  print "Parent pid is: %d" % (cur_pid)
            child.setPid(os.getpid())
            child.Run()

pr = Parent()

#pr.writeToQueue()
pr.CreateChild()
pr.CreateChild()


   
