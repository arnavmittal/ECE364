import sys
import os
import re

def edit_email():
    expr = r"([\w._-]*)@purdue.edu\s+(\d+.\d+)"
    with open("Part2.in") as inputFile:
        content = inputFile.readlines()
        for line in content:
            matched = re.search(expr,line)
            if matched:
                output=matched.group(1)+"@ecn.purdue.edu"+"\t"+matched.group(2)+"/100"
                print(output)
    return 0

if __name__ == "__main__":
    edit_email()

