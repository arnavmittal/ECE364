#!/usr/bin/env python3

import sys
import os
import re

def finder(filename):
    expr=('def(\s)*([a-zA-Z][\w-]+)(\s)*\(([\s\w,=-]+)\):')
    if(not os.path.isfile(filename)):
        print("Error: File "+filename+" does not exist")
        return 0

    if(not os.access(filename, os.R_OK)):
        print("Error: Could not read "+filename)
        return 0

    with open(filename) as inputFile:
        content = inputFile.readlines()
        for line in content:
            matched = re.search(expr,line)
            if matched:
                print (matched.group(2))
                output = matched.group(4).split(',')
                count=1
                for i in range(len(output)):
                    new_str="Arg"+str(count)+": "+output[i].strip()
                    count+=1
                    print(new_str)

    return 0

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage: function_finder.py [python_file_name]")
        quit()

    filename = sys.argv[1]
    finder(filename)