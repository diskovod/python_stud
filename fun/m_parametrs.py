#!/usr/bin/env python

class getMultipleParametrs(object):
    def __init__(self):
        pass


    def total(initial=5, *numbers, **keywords):
        count = initial
        print numbers
        print keywords
        for number in numbers:
            count += number
        for key in keywords:
            count += keywords[key]
        return count


multiple_parametrs = getMultipleParametrs()
multiple_parametrs.total(10,1,2,3,4, vegetables=50, fruits=100)
