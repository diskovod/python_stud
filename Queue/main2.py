#!/usr/local/bin/python

import datetime
import os
import time
from multiprocessing import Queue
from multiprocessing import Process


class Child(object):
    def __init__(self):
        pass
        #signal.signal(signal.SIGTERM, self.child_signal_handler)

   # def child_signal_handler(self, signal, frame):
       
   #     isClosed = os.kill(self.pid, 0)

    #    if isClosed == None:

     #       print "Child %d closed!" % (self.pid)
     #       sys.exit(0)
        
      #  else:

       #     print "Child still working..."

    def setPid(self, pid):
        self.pid = pid

    def Run(self, queue):
        self.alive = True
        while True:
            
            print "Timestamp: %s, Child_id: %s" % (queue.get(), self.pid)


class Parent(object):
    def __init__(self):
        self.q = Queue()
        self.childlist = []

    def writeToQueue(self):
        
        while True:
            
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            self.q.put(st)

            #print self.q.get()
            time.sleep(1)

    def CreateChild(self):
        child = Child()
        cur_pid = os.getpid()

        pid = os.fork()
        if pid > 0:
            
            self.childlist.append(pid)
        
        else:
        
          #  print "Parent pid is: %d" % (cur_pid)
            child.setPid(os.getpid())
            child.Run(self.q)

pr = Parent()

#pr.writeToQueue()
pr.CreateChild()
pr.CreateChild()


   
