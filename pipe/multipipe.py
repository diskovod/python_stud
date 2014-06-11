#!/usr/local/bin/python

import datetime
import os
import time
from multiprocessing import Queue
from multiprocessing import Process, Pipe
from Queue import Empty
import signal
import sys
import threading


class Child (Process):
    def __init__(self, chld_name, conn):
        Process.__init__(self)
        self.conn = conn
        self.chld_name = chld_name
      #  self.event = event

    def child_signal_handler(self):
        

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

        print os.getpid()
        print "I'm child, reading pipe...."
        print self.conn.recv()
        

#       with open(self.pipe_name, 'r') as pipein:
#
#       #     while not self.event.is_set():
#            
#            line = pipein.readline()[:-1]
#
#            print "Child %d got %s" % (os.getpid(), line)
#            
#        #        time.sleep(2)


class Parent(object):
    def __init__(self, conn):
        
        self.conn = conn
        self.event = threading.Event()
      #  self.pipe_name = "/work/work_1/test_pipe.txt"

      #  self.child_1 = Child("Child-1", par_conn, self.event)

        signal.signal(signal.SIGTERM, self.signal_term_handler)

        self.cur_pid = os.getpid()

    def writeToPipe(self):

            print "I'm parent %d, sending data" % (os.getpid())

            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            self.conn.send(st)
            self.conn.close()
            
    def TerminateAll(self):

        if self.termProc == True:

            #for child in self.childlist:
            print "Terminate child: %s" % (self.child_1.name)
            self.child_1.terminate()

         #   print "Terminate child: %s" % (self.child_2.name)
         #   self.child_2.terminate()
         #   sys.exit(0)
            #os.kill(l)

        else:
            pass

    def signal_term_handler(self, signal, frame):

        self.termProc = True
        self.event.set()
        print 'got SIGTERM, Event started'
        self.TerminateAll()

   # def RunChild(self):
   #     
   #     print "Parent pid is: %s" % (self.cur_pid)
   #      
   #     self.child_1.start()

   # def deleteFifo(self):
   #     if os.path.exists(self.pipe_name):
   #    
   #         try:

   #             os.unlink(self.pipe_name)

   #         except OSError as e:

   #             print "Cant delete Fifo. {0} ".format(e.strerror)

    def sendPipeName(self):

        return self.pipe_name

class Mother(object):
    def __init__(self, chld_conn):
        
        self.child = Child("Child_1", chld_conn)

    def RunChild(self):

        print "Child started"

        self.child.start()



parent_conn, child_conn = Pipe()

pr = Parent(parent_conn)


#pipe_name = pr.sendPipeName()

mt = Mother(child_conn)

pr.writeToPipe()

mt.RunChild()





    
    

        
#pr.writeToQueue()
