#!/usr/local/bin/python

import datetime
import os
import time
from multiprocessing import Queue
from multiprocessing import Process


class Parent(object):
    def __init__(self):
        self.q = Queue()

    def writeToQueue(self):
        
        while True:
            
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            self.q.put(st)

            print self.q.get()
            time.sleep(1)


    def processInfo(self):
        
        print('process id:', os.getpid())

    def readingQueue(self):
        self.info()
        print('hello', name)



if __name__ == '__main__':
    pr = Parent()
    pr.getParentPid()
    print "====================="
    pr.info()
    p = Process(target=pr.f, args=('bob',))
    p.start()
    p.join()
    pr.info()
    p1 = Process(target=pr.f, args=('steve',))
    p1.start()
    p1.join()


        
#pr.writeToQueue()
