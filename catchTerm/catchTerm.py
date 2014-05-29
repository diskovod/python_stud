import signal
import sys
import time


def signal_term_handler(signal, frame):
    print 'got SIGINT'

    sys.exit(0)
 
signal.signal(signal.SIGINT, signal_term_handler)
time.sleep(10)
