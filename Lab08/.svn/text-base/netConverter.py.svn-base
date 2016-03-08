from HardwareTasks import *

def verilog2vhdl(ver_line):
    try:
        (comp_name, inst_name, values) = processLine(ver_line)
    except ValueError:
        return("Error: Bad Line.")
    #print(comp_name)
    #print(inst_name)
    #print(values)
    new_str = ""
    new_str += inst_name+": "+comp_name+" PORT MAP("
    i=0
    for (x, y) in values:
        i+=1
        new_str+=x+"=>"+y
        if i != len(values):
            new_str+=", "
    new_str+=");"
    return new_str

def convertNetlist(sourceFile, targetFile):
    with open(sourceFile) as inputFile:
        content = inputFile.readlines()
        i=0
        new_str=""
        for data in content:
            i+=1
            new_str += verilog2vhdl(data)
            if i != len(content):
                new_str+= "\n"
    print(new_str)
    with open(targetFile, "w") as outputFile:
        outputFile.write(new_str)

