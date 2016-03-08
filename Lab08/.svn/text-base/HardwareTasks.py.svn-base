import re

def idIsAcceptable(ver_id):
    expr1 = r"[\w]+$"
    matched1 = re.match(expr1,ver_id)
    if matched1:
        return True
    else:
        return False


def processSingle(ver_assignment):
    expr1 = r"\.([\w]+)\(([\w]+)\)$"
    matched1 = re.match(expr1,ver_assignment)
    if matched1:
        valid_1 = idIsAcceptable(matched1.group(1))
        valid_2 = idIsAcceptable(matched1.group(2))
        if (valid_1 and valid_2):
            return (matched1.group(1), matched1.group(2))
    else:
        raise ValueError(ver_assignment)

def processLine(ver_line):
    #print(ver_line)
    expr1 = r"\s*([\w]+)\s+([\w]+)\s+\(\s*(.*)\s*\)"
    matched1 = re.match(expr1,ver_line)
    if matched1:
        #print(matched1.group(1))
        #print(matched1.group(2))
        #print(matched1.group(3))
        valid_1 = idIsAcceptable(matched1.group(1))
        valid_2 = idIsAcceptable(matched1.group(2)) and matched1.group(2 is not "")
        valid_3 = (matched1.group(3) is not "")
        if not(valid_1 and valid_2 and valid_3):
            raise ValueError(ver_line)
        input_list = matched1.group(3).split(",")
        new_list=[]
        for x in input_list:
            new_list.append(x.strip())
        new_tuple=()
        for x in new_list:
            new_tuple += (processSingle(x) ,)
        return (matched1.group(1), matched1.group(2), new_tuple)
    else:
        raise ValueError(ver_line)

