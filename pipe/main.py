#!/usr/local/bin/python


import datetime
import os
import time
import signal
import sys
import threading


class Child (threading.Thread):
    def __init__(self, chld_name, pipe_name, e):
        threading.Thread.__init__(self)
        self.pipe_name = pipe_name
        self.chld_name = chld_name
        self.event = e

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

        print "Starting " + self.name
        
        with open(self.pipe_name, 'r') as pipein:

            while not self.event.is_set():
            
                line = pipein.readline()[:-1]

                print "Child %d got %s" % (os.getpid(), line)
            
                time.sleep(2)

class Parent(object):
    def __init__(self):

        self.pipe_name = "/work/work_1/test_pipe.txt"
        
        self.event = threading.Event()

        self.child_1 = Child("Child-1", self.pipe_name, self.event)
      #  self.child_2 = Child("Child-2", self.q, self.event)
        
        signal.signal(signal.SIGTERM, self.signal_term_handler)
        
        self.cur_pid = os.getpid()

    def writeToFifo(self):
            
        if not os.path.exists(self.pipe_name):
       
            try:

                os.mkfifo(self.pipe_name, 0777)

            except OSError as e:

                print "Cant create FiFo file. {0} ".format(e.strerror)


     #   while True:
        print "Open write"  
        with open(self.pipe_name, 'w') as pipeout:

            print "Opened write"
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            pipeout.write(st)
            
           # pipeout.close()

            #    time.sleep(1)

    def TerminateAll(self):

        if self.termProc == True:

            print "Terminate child: %s" % (self.child_1.name)

           # print "Terminate child: %s" % (self.child_2.name)
            sys.exit(0)

        else:
            pass

    def signal_term_handler(self, signal, frame):
        
        self.event.set()
        self.termProc = True
        print 'got SIGTERM, Event started'
        self.TerminateAll()

    def RunChild(self):
        
        
        print "Parent pid is: %s" % (self.cur_pid)
         
        self.child_1.start()

    def readFifo(self):
        
        
        with open(self.pipe_name, 'r') as pipein:
            print "access"


          #  while True:
            
            line = pipein.readline()

            print "Child %d got %s" % (os.getpid(), line)
l
    def deleteFifo(self):

        os.unlink(self.pipe_name)


pr = Parent()

#pr.deleteFifo()
pr.writeToFifo()
pr.RunChild()
#pr.readFifo()




    
    

        
#pr.writeToQueue()
