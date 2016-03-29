import re
def getAddress(sentence):
    expr1=r"(\w{2})[:-]+(\w{2})[:-]+(\w{2})[:-]+(\w{2})[:-]+(\w{2})[:-]+(\w{2})"
    matched1=re.search(expr1, sentence)
    print(sentence)
    if matched1:
        for i in [1,2,3,4,5,6]:
            for j in [0,1]:
                if(matched1.group(i)[j] not in ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','A','B','C','D','E','F']):
                    return None
        print(matched1.group(0))
        return(matched1.group(0))
    else:
        return None

def getSwitches(commandline):
    expr1=r"+?\?(.*)\s*(.*)"
    matched1=re.search(expr1,commandline)
    print(commandline)
    if matched1:
        print(matched1.group(1))
    else:
        return None

def getElements(fullAddress):
    expr1=r"https?://(.*)/([a-zA-Z0-9]*)/([a-zA-Z0-9]*)(.*)$"
    matched1=re.search(expr1,fullAddress)
    if matched1:
        for element in matched1.group(1):
            if element is "/":
                return None
        if matched1.group(4) is not "":
            return None
        return (matched1.group(1), matched1.group(2), matched1.group(3))
    else:
        return None