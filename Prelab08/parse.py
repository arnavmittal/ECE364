#!/usr/bin/env python3
import sys
import os
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage: parse.py [filename]")
        quit()

    filename = sys.argv[1]
    if(not os.access(filename, os.E_OK)):
        print("{} is not a readable file ".format(filename))
        quit()