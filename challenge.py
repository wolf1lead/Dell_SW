#!/usr/bin/env python
#
# This Python file uses the following encoding: utf-8
""" docstring

This module accepts an input text file and reads each line to find the
biggest word. It then prints outs the biggest word forwards and reverse.

Usage: python challenge.py <file>

"""
import os
import sys

def check_file(input_file):
    """ Check for IN_FILE in the current directory. """
    if (os.path.exists(input_file)) and (os.path.isfile(input_file)) \
            and (os.path.getsize(input_file)):
        return True
    else:
        raise Exception('File not found.')

def find_big_word(input_file):
    """ Open the file, read each line and find the biggest word. """
    with open(input_file, 'r') as search_file:

        # Initialize WORD_LENGTH.
        word_length = 0

        # Check the word length and save the biggest word.
        for word in search_file:
            if len(word) > word_length:
                word_length = len(word)
                big_word = word

        # Print out the big word forwards.
        print("Big word %s ") % big_word.strip('\n')

        # Print out the big word backwards.
        print("Reversed %s ") % big_word[::-1].strip('\n')

    search_file.close()

if __name__ == '__main__':
    # Get and check input arguments.
    if len(sys.argv) >= 2:
        FILE = sys.argv[1]
    else:
        print("\nUsage: %s <file>") % sys.argv[0]
        exit()

check_file(FILE)
find_big_word(FILE)
