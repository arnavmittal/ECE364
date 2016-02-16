
def rowSumIsValid(mat):
    #print(mat)
    addition=0
    t_sum=[]
    for i in mat:
        for j in i:
            addition+=int(j)
        t_sum.append(addition)
        addition=0
        new_set = set(t_sum)
    if len(new_set)==1:
        return True
    return False

def columnSumIsValid(mat):
    t_sum=[]
    f_sum=[]
    for i in mat:
        length=len(i)
        for j in i:
            t_sum.append(j)

    for n in range(0,length):
        f_sum.append(0)
    for m in range(0,len(t_sum)):
        f_sum[m%length]+=t_sum[m]
    new_set = set(f_sum)
    if len(new_set)==1:
        return True
    return False

def magicSquareIsValid(mat):
    new_list=[]
    k=[]
    with open(mat) as inputFile:
        content=inputFile.readlines()
    for i in content:
        j=i.split()
        if("\n" in j):
            j.remove("\n")
        k=[int(x) for x in j]
        new_list.append(k)

    check1=rowSumIsValid(new_list)
    check2=columnSumIsValid(new_list)
    if(check1 and check2):
        return True
    return False

def getTotalCost(itemSet):
    return 0

def getBestPrices(cpuSet):
    return 0

def getMissingItems():
    return 0