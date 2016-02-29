import decimal
import sys
import os

class PointND:
    def __init__(self,*args):
        self.t= args
        self.n = len(args)
        for element in args:
            if type(element) != float:
               raise ValueError("Cannot instantiate an object with non-float values.")

    def __str__(self):
        current=1
        string="("
        for element in self.t:
            if current == len(self.t):
                string+='{0:.2f}'.format(element)
            else:
                string+='{0:.2f}'.format(element)
                string+=", "
            current+=1
        string+=")"
        return string

def main():
    pass
    p1 = PointND(6.9584, 2.7017, 3.1415)
    #p2 = PointND(1.1,12,1.3)
    print(p1.n)
    print(p1.t)
    print(p1.__str__())

if __name__ == "__main__" :
    main()
