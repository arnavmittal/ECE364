def getPairwiseDifference(vec):
    new_vec=[]
    if (type(vec) is not list):
        return(None)

    if (len(vec) == 0):
        return(None)

    for i in range(0,len(vec)-1):
        new_vec.append(vec[i+1]-vec[i])
    return(new_vec)

def flatten(l):
    if (type(l) is not list):
        return(None)

    for i in l:
        if (type(i) is not list):
            return(None)
    new_list=[]
    for j in l:
        for k in j:
            new_list.append(k)
    return(new_list)

def partition(l,n):
    if (type(l) is not list):
        return(None)

    if (len(l) == 0):
        return(None)

    new_list=[]
    sublist=[]

    length_l=0
    count=n
    for i in l:
        length_l=length_l+1
        if(count != 0):
            count=count-1
            sublist.append(i)
        if(count == 0 or length_l == len(l)):
            count=n
            new_list.append(sublist)
            sublist=[]
    return(new_list)

def rectifySignal(signal):
    if (type(signal) is not list):
        return(None)

    if (len(signal) == 0):
        return(None)

    new_list=[]

    for i in signal:
        if(i < 0):
            new_list.append(0)
        else:
            new_list.append(i)

    return(new_list)

def floatRange(a,b,s):
    if ( float(a) >= float(b)):
        return(None)
    sum=float(a)
    new_list=[]
    num=(float(b)-float(a))/float(s)
    for i in range(int(num)+1):
        new_list.append(sum)
        sum=round(float(sum)+float(s),2)
    return(new_list)

def getLongestWord(sentence):
    if (type(sentence) is not str):
        return(None)

    new_sen=sentence.split()

    if (len(new_sen) <= 1):
        return(None)

    max_len=0
    max_word=""
    for i in new_sen:
        if (len(i) >= max_len):
            max_len=len(i)
            max_word=i
    return (max_word)

def decodeNumbers(numList):
    if (type(numList) is not list):
         return(None)

    new_string=""
    for i in numList:
        if (type(i) is not int):
            print (i)
            return(None)

    for j in numList:
        new_string+=chr(j)

    return(new_string)

def getCreditCard(s):
    if (len(s) == 0):
        return None
    list=[]
    for i in s:
        if(ord(i)>= 48 and ord(i)<= (48+9)):
            list.append(int(i))

    return(list)