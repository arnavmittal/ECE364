class Simulation:
    def __init__(self, simnNo, simDate, chipName, chipCount, chipCost):
        self.simulationNumber = simnNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount = chipCount
        self.chipCost = chipCost
        self.simulationCost = self.chipCost * self.chipCount

    def __str__(self):
        new_str=""
        new_str+= self.chipName
        new_str += ": "
        new_str += ("{0:03d}").format(self.simulationNumber)
        new_str += ", "
        new_str += self.simulationDate
        new_str += ', $'
        new_str += ("{0:06.2f}").format(self.simulationCost)
        return new_str

class Employee:
    def __init__(self, employeeName, employeeID):
        self.employeeName = employeeName
        self.employeeID = employeeID
        self.simulationsDict = {}

    def addSimulation(self, sim):
        if sim.simulationNumber in self.simulationsDict.keys():
            self.simulationsDict[sim.simulationNumber] = sim
        else:
            self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self, simNo):
        if simNo in self.simulationsDict.keys():
            return self.simulationsDict[simNo]
        else:
            return None

    def __str__(self):
        new_str=""
        new_str+=self.employeeID
        new_str+=", "
        new_str+=self.employeeName
        new_str+=": "
        new_str+=("{0:02d}").format(len(self.simulationsDict))
        new_str+= " Simulations"
        return new_str

    def getWorkload(self):
        new_str=""
        new_str+=str(self)
        new_str+="\n"
        i=0
        new_list=[]
        for element in self.simulationsDict.keys():
            new_list.append(str(self.simulationsDict[element]))
        new_list.sort()
        for item in new_list:
            new_str+=item
            i+=1
            if (i != len(self.simulationsDict.keys())):
                new_str+="\n"
        print(new_str)
        return  new_str

    def addWorkload(self,fileName):
        with open(fileName) as inputFile:
            content = inputFile.readlines()
            for line in content[2:]:
                new_list = line.split()
                conv=new_list[4]
                new_list[4]=conv[1:]
                thing=Simulation(int(new_list[0]),new_list[1],new_list[2],int(new_list[3]),float(new_list[4]))
                self.addSimulation(thing)

class Facility:
    def __init__(self, facilityName):
        self.facilityName = facilityName
        self.employeesDict = {}

    def addEmployee(self, employee):
        if employee.employeeName in self.employeesDict.keys():
            self.employeesDict[employee.employeeName] = employee
        else:
            self.employeesDict[employee.employeeName] = employee

    def getEmployees(self, *args):
        new_list=[]
        for value in args:
            new_list.append(self.employeesDict[value])
        return new_list

    def __str__(self):
        new_str=""
        new_str+=self.facilityName+": "+("{0:02d}").format(len(self.employeesDict))+" Employees"
        new_str+="\n"
        i=0
        new_list=[]
        for element in self.employeesDict.keys():
            new_list.append(str(self.employeesDict[element]))
        print(new_list)
        new_list.sort()
        for item in new_list:
            new_str+=item
            i+=1
            if (i != len(self.employeesDict.keys())):
               new_str+="\n"
        print(new_str)
        return new_str

    def getSimulation(self, simNo):
        for employee in self.employeesDict:
            emplvalue=self.employeesDict[employee]
            for simabc in emplvalue.simulationsDict:
                if simNo == emplvalue.simulationsDict[simabc].simulationNumber:
                    return emplvalue.simulationsDict[simNo]
        return None

