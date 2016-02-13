
import sys
import os
import string
import glob
import filecmp

# ===========PART 2===========\

def importFilenames2():

    filenames = glob.glob('purchases/purchase_*')
    return filenames

def getPurchaseReport():
    filenames = importFilenames2()
    items = []
    with open('purchases/Item List.txt', 'r') as itemList:
        for line in itemList:
            items.append(line)

    sumDict = {}
    for file in filenames:
        sum = 0
        with open( file, 'r' ) as inputFile:
            allLines = inputFile.readlines()
            transactionLines = allLines[2:]
            for line in transactionLines:
                parts = line.split()
                sum += float(parts[1])
        #print file
        sumDict[file[19:22]] = float(sum)
    #print sumDict
    return sumDict

def makedic(filename):
    dicto = {}
    with open(filename,"r") as readfile:
        for line in readfile:
            splitline = line.split()
            if(len(splitline)) == 2:
                product = splitline[0]
                price = splitline[1]

                dicto[product] = price
    return dicto

def getTotalSold():
    dictionary = {}
    files = glob.glob('./purchases/*')
    files.remove('./purchases/Item List.txt')
    pricedict = makedic('./purchases/Item List.txt')
    keys = pricedict.keys()
    for each in keys:
        if each != "Name":
            sum2 = 0
            for name in files:
                purdict = makedic(name)

                if each in purdict:
                    sum2 += float(purdict[each])

                dictionary[each] = sum2
    #print dictionary
    return dictionary

def main():

    #getWordFrequency()
    #getDuplicates()
    getPurchaseReport()

if __name__ == "__main__" :
    main()

