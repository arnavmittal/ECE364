import os
from glob import glob

def make_dict():

    temp_dict = {}
    with open('files/students.txt') as input:
        lines = input.readlines()
        for lines in lines[2:]:
            line = lines.split('|')
            name = line[0].strip()
            id = line[1].strip()
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

def getStudentList(classNumber):
    list_name=[]
    open_file='files/EECS'
    open_file+=classNumber
    open_file+='.txt'
    dict_std=make_dict()
    #print(dict_std)
    if not os.path.exists(open_file):
        return[]
    with open(open_file) as file:
        data=file.readlines()
        for i in range(2,len(data)):
            data_line=data[i].split()
            key = dict_std[data_line[0]]
            list_name.append(key)
    list.sort(list_name)
    return list_name

def searchForName(studentName):
    course_files= glob('files/EE*')
    dict_std=make_dict()
    dict_score={}
    for course in course_files:
        with open(course) as file:
            data=file.readlines()
            for i in range(2,len(data)):
                data_line=data[i].split()
                if studentName == dict_std[data_line[0]]:
                    key = course[10:13]
                    dict_score[key] = int(data_line[1])
    return dict_score


def searchForID(studentID):
    dict_std=make_dict()
    if studentID in dict_std:
        std_name = dict_std[studentID]
    else:
        return {}

    dict_score = searchForName(std_name)
    return dict_score

def findScore(studentName, classNumber):
    open_file='files/EECS'
    open_file+=classNumber
    open_file+='.txt'
    dict_std=make_dict()
    #print(dict_std)
    if not os.path.exists(open_file):
        return[]
    dict_std=make_dict()
    with open(open_file) as file:
        data=file.readlines()
        for i in range(2,len(data)):
            data_line = data[i].split()
            name = dict_std[data_line[0]]
            if name == studentName:
                return int(data_line[1])
    return None

def getHighest(classNumber):
    FileName = 'files/EECS%s.txt'%classNumber
    max = 0.0
    name = ""
    if not os.path.exists(FileName):
        return ()
    Student_dict = make_dict()
    with open(FileName) as fp:
        Content = fp.readlines()
        for I in range(2, len(Content)):
            ContentFile = Content[I].split()
            if int(ContentFile[1]) > max:
                max = float(ContentFile[1])
                name = Student_dict[ContentFile[0]]
    return (name, max)

def getLowest(classNumber):
    FileName = 'files/EECS%s.txt'%classNumber
    min = 100000000.00
    name = ""
    if not os.path.exists(FileName):
        return ()
    Student_dict = make_dict()
    with open(FileName) as fp:
        Content = fp.readlines()
        for I in range(2, len(Content)):
            ContentFile = Content[I].split()
            if int(ContentFile[1]) < min:
                min = float(ContentFile[1])
                name = Student_dict[ContentFile[0]]
    return (name, min)

def getAverageScore(studentName):
    Student_dict = make_dict()
    sum = 0
    avg = 0.0
    num = 0
    FileList = glob('files/EE*')
    for I in FileList:
        with open(I) as fp:
            Content = fp.readlines()
            for J in range(2, len(Content)):
                ContentFile = Content[J].split()
                if Student_dict[ContentFile[0]] == studentName:
                    sum += int(ContentFile[1])
                    num += 1
    if num == 0:
        return None
    avg = sum / num
    return avg


