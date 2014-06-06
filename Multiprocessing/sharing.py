#!/usr/local/bin/python

from multiprocessing import Process, Manager

def child(d):
    d[1] += '1'
    d['2'] += 2


if __name__ == '__main__':
    manager = Manager()

    d = manager.dict()
    d[1] = '1'
    d['2'] = 2

    p1 = Process(target=child, args=(d,))
    p2 = Process(target=child, args=(d,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print d
