from glob import glob

def getCallActivity():
    return 0

def getCallersOf(Number):
    dict_std=make_dict()
    dict_caller={}
    with open('Call Log.txt') as inputLog:
        all_lines = inputLog.readlines()
        for all_lines in all_lines[2:]:
            line = all_lines.split()
            key = ' '.join(line[0:2])
            match_1=line[3]
            match=match_1[4:]
            #still working here
            print("HERE I AM")
    return 0

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

def getDetails():
    course_files= glob('files/EE*')
    dict_std=make_dict()
    dict_score={}
    crs_num=''
    for course in course_files:
        crs_num=course[10:13]
        with open(course) as curr_crs_file:
            data = curr_crs_file.readlines()
            #print (data)
            for i in range(2,len(data)):
                data_line=data[i].split()
                #print (data_line)
                key = dict_std[data_line[0]]
                tup1 = (crs_num, int(data_line[1]))
                if key in dict_score:
                    dict_score[key].add(tup1)
                else:
                    dict_score[key]={tup1}
    #print (dict_score)
    return dict_score

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
