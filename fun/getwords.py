#!/usr/bin/env python

import re
import sys

class getWords(object):
    def __init__(self):
        pass

    def main(self):
        pattern = "(\s)"

        while True:
            s = raw_input('Input word: ')
            spaces_count = re.findall(pattern,s)
            
            final_word_count = len(s) - len(spaces_count)

            print "You input: %s; word count is: %s" % (s,final_word_count)
            #print "Do you want to continue? (Yes/No)"
            choice = raw_input('Do wou want to continue? (Yes/No): ')
            if (choice == 'yes' or choice == 'Yes'):
                continue
            else:
                break

            if (s == 'exit'):
                print "Exiting program"
                break

get_words = getWords()
get_words.main()
