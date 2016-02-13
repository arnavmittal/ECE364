from glob import glob
import filecmp
import re

def getWordFrequency():
    temp_dict={}
    files = glob('./files/*')
    for afile in files:
        with open(afile, 'r') as readafile:
            for line in readafile:
                for word in line.split():
                    i=word[0]
                    proceed=0
                    if(i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z'):
                        proceed=1
                    if(proceed):
                        if word in temp_dict:
                            temp_dict[word]+=1
                        else:
                            temp_dict[word]=1
    return temp_dict

def check_samefile(file, all_files):
    new_list=[]
    check=0
    for temp_file in all_files:
        if file != temp_file:
            check=filecmp.cmp(file,temp_file)
            if (check):
                new_list.append(temp_file[8:11])
    new_list.append(file[8:11])
    list.sort(new_list)
    return new_list

def getWordCount(filename):
    word_count=0
    final_string=""
    new_file="./files/"
    new_file+=filename
    new_file+=".txt"
    freq={}
    all_files = glob('./files/*')

    with open(new_file, 'r') as original:
        text=original.read()
        text=text.replace(",", "")
        text=text.replace(".", "")
        text=text.replace(";", "")
        if(freq.get(text) is None):
            wordArr = text.split()
            wordSet = set(wordArr)
            uniquewords=len(wordSet)
    return uniquewords


def getDuplicates():
    final_dict={}
    read_files=[]
    all_files = glob('./files/*')
    for file in all_files:
        if(file not in read_files):
            read_files.append(file)
            temp_list = check_samefile(file, all_files)
            if(len(temp_list) > 1):
                wordcount = getWordCount(temp_list[0])
                mid_key=temp_list[0]
                final_key=mid_key
                final_value=(wordcount, temp_list)
                final_dict[final_key]=final_value
    return final_dict

def getPurchaseReport():
  master = {}
  all_files = glob('./purchases/*')
  done = []
  for file in all_files:
    research = re.search('./purchases/purchase_(.*).txt', file)
    if research:
      done.append(research.group(1))

  item_list = "Item List"
  with open("./purchases/" + item_list + ".txt") as file:
      value = file.read()
      value = value.split()
      value = value[3:]
      length = len(value)
      for i in range(0,length,2):
        master[value[i]] = float(value[i+1][1:])

  numbers = []

  for item in done:
    with open("./purchases/purchase_" + item + ".txt") as file:
      value = file.read()
      value = value.split()
      value = value[3:]
      length = len(value)
      quantities = {}
      for i in range(0, length, 2):
        quantities[value[i]] = int(value[i+1])
      numbers.append(quantities)

  i = 0
  final = {}
  for item in done:
    final[int(item)] = cost_calcu(numbers[i], master)
    i += 1
  return(final)


def cost_calcu(values, master):

  cost = 0
  for key in values:
      cost += master[key] * values[key]
  cost = round(cost, 2)
  return(cost)


def getTotalSold():
  done = []
  all_files = glob('./purchases/*')
  for file in all_files:
    research = re.search('./purchases/purchase_(.*).txt', file)
    if research:
      done.append(research.group(1))

  numbers = []

  for item in done:
    with open("./purchases/purchase_" + item + ".txt") as file:
      value = file.read()
      value = value.split()
      value = value[3:]
      length = len(value)
      quantities = {}
      for i in range(0, length, 2):
        quantities[value[i]] = int(value[i+1])
      numbers.append(quantities)

  dict = {}

  length = len(numbers)

  for i in range(length):
    for key in numbers[i]:
      try:
        dict[key] += numbers[i][key]
      except:
        dict[key] = numbers[i][key]

  return(dict)