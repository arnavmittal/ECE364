from glob import glob

def getCallActivity():
    dict_std=make_dict()
    dict_time={}
    dict_final={}
    with open('Call Log.txt') as inputLog:
        all_lines = inputLog.readlines()
        for lines in all_lines[2:]:
            line = lines.split()
            match_1=line[1]
            match=match_1[4:]
            value=line[4]
            if match not in dict_time:
                dict_time[match]= [value]
            else:
                dict_time[match].append(value)

        for key in dict_time:
            min=0
            sec=0
            numb=len(dict_time[key])
            for i in dict_time[key]:
                data = i.split(":")
                min+=int(data[0])
                sec+=int(data[1])
            fin_sec=sec%60
            fin_min=int(min+sec/60)
            fin_hr=int(fin_min/60)
            fin_min=fin_min%60
            new_str=""
            if(fin_hr <= 9):
                new_str+="0"
            new_str+=str(fin_hr)
            new_str+=":"
            new_str+=str(fin_min)
            new_str+=":"
            new_str+=str(fin_sec)
            dict_time[key]=(numb,new_str)
        for keys in dict_std:
            new_key = dict_std[keys]
            new_value = dict_time[keys]
            dict_final[new_key]=new_value

    return dict_final

def getCallersOf(Number):
    dict_std=make_dict()
    dict_caller={}
    with open('Call Log.txt') as inputLog:
        all_lines = inputLog.readlines()
        for lines in all_lines[2:]:
            line = lines.split()
            key = ' '.join(line[2:4])
            match_1=line[1]
            match=match_1[4:]
            new_set={}
            if key in dict_caller:
                if dict_std[match] not in dict_caller:
                    if(dict_std[match] not in dict_caller[key]):
                        dict_caller[key].append(dict_std[match])
                        dict_caller[key].sort()
            else:
                    dict_caller[key]=[dict_std[match]]
            #print("DEBUG HERE")
            #still working here
        #print("HERE I AM")
    return dict_caller.get(Number, [])

def make_dict():
    temp_dict = {}
    with open('Students.txt') as input:
        lines = input.readlines()
        for lines in lines[2:]:
            line = lines.split('|')
            name = line[0].strip()
            id = line[1].strip()
            id = id.replace("x","")
            temp_dict[id] = name
    return temp_dict

def solvePuzzle(sourceFile, TargetFile):
    #print(sourceFile)
    with open(sourceFile) as inputFile:
        all_lines = inputFile.readlines()
        count=0
        line_count=0
        column=[45,45,45,45,45,45,45,45,45]
        if(all_lines[0].find('.')!=-1):
            #1 COLUMN is '.', hence ROW METHOD
            for line in all_lines:
                count+=1
                miss_value=45
                out_line=list(line)
                out_line.remove('.')
                if count != 9:
                    out_line.remove('\n')
                for i in out_line:
                    miss_value-=int(i)
                miss_str = str(miss_value)
                line=line.replace(".",miss_str)
                with open(TargetFile, 'a') as outputFile:
                    outputFile.write(line)
        else:
            #1 ROW is missing '.', hence COLUMN METHOD
            for line in all_lines:
                count+=1
                if(line.find('.')!=-1):
                    line_count=count
                    continue
                else:
                    out_line=list(line)
                    if count != 9:
                        out_line.remove('\n')
                    for i in range(0,9):
                        column[i]-=int(out_line[i])
            new_column=[str(j) for j in column]
            if(line_count != 9):
                new_column.append('\n')
            out_str=''.join(new_column)
            new_count=0
            for line in all_lines:
                with open(TargetFile, 'a') as outputFile:
                    new_count+=1
                    if(new_count!=line_count):
                        outputFile.write(line)
                    else:
                        outputFile.write(out_str)
    return 0

def verifySolution(filename):
    with open(filename) as inputFile:
        all_lines = inputFile.readlines()
        count=0
        column=[45,45,45,45,45,45,45,45,45]
        for line in all_lines:
            #print(line)
            sum=45
            for i in range(0,9):
                sum-=int(line)%10
                column[i]-=int(line)%10
                line = int(int(line)/10)
            if(sum==0):
                count+=1

        if(count == 9):
            for k in range(0,9):
                if (column[k]!=0):
                    return False
            return (True)
    return (False)
