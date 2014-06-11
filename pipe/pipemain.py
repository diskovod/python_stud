import datetime
import os
import time
import signal
import sys
import threading
import tempfile
import select
import stat

class Consumer (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.pipe = None
        self.pipefd = None
        self.name = name

    def setPipe(self, pipe_name):
        self.pipe = pipe_name

    def connectPipe(self, pipe_name):
        self.pipe = pipe_name
        self.pipefd = os.open(self.pipe, os.O_RDONLY | os.O_NONBLOCK)

    def run(self):
        print "Starting " + self.name
        p = select.poll()
        p.register(self.pipefd, select.POLLIN)
        while True: 
            events = p.poll(100)
            for e in events:
                line = os.read(self.pipefd, 255)
                if len(line) == 0:
                   continue
            
                print "Child %s(%d) receive: %s" % (self.name, os.getpid(), line)
        pipein.close()

class Producer (object):
    def __init__(self, directory):
        self.directory = directory
        self.pipes = []

    def registerConsumer(self, consumer):
        pipe_dir = tempfile.mkdtemp(prefix='pipe_', suffix='/', dir=self.directory)
        pipe_path = os.path.join(pipe_dir, 'fifo')
        
        try:
            os.mkfifo(pipe_path, 0777)
        except OSError, e:
            print "Failed to create FIFO: %s" % e
        else:
            consumer.connectPipe(pipe_path)
            new_pipefd = os.open(pipe_path, os.O_WRONLY | os.O_NONBLOCK)
            self.pipes.append(new_pipefd)
            print "Consumer %s registered" % (consumer.name)

    def start(self):
        while True:
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            for pipefd in self.pipes:
               os.write(pipefd, st) 

            time.sleep(2)

class Controller (object):
    def __init__(self, tmp_directory):
        self.path = tmp_directory
        try:
            print 'Create temp directory'
            os.mkdir(self.path)
        except Exception as e:
            print e
        self.producer = Producer(self.path)
        self.consumers = []
    
        for i in range(2):
            c = Consumer('Consumer[%d]' % (i))
            self.producer.registerConsumer(c)            
            self.consumers.append(c)

    def start(self):
        for c in self.consumers:
            c.start()

        self.producer.start()
        
print '[START]'
controller = Controller('/home/j2ko/Project/j2ko/python_stud/j2ko/pipe/tmp_pipe/')
controller.start()
print '[END]'

   






