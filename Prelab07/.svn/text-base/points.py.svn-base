import decimal
import sys
import os
from math import sqrt
import copy

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

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        t_sum=0
        #print(self.t)
        #print(other.t)
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        for element1, element2 in zip(self.t, other.t):
            t_sum+=(element1-element2)**2
        t_sum=sqrt(t_sum)
        return t_sum

    def nearestPoint(self, points):
        minimum=1000000.00
        dist_dict={}
        if len(points)==0:
            raise ValueError("Input cannot be empty.")
        for apoint in points:
            dist = self.distanceFrom(apoint)
            dist_dict[dist]=apoint
            if dist < minimum:
                minimum = dist
        return dist_dict[minimum]

    def clone(self):
        q = copy.deepcopy(self)
        return q
    #//////////////////////////////////PROBLEM SOMEWHERE HERE////////////////////////////////////
    def __add__(self, other):
        print(type(other))
        if isinstance(self, other):
            print(self.t+other.t)
            return PointND(self.t + other.t)
        else:
            print(self.t+other)
            return PointND(self.t + other)
        #copied = []
        #if type(other) == float:
        #    for element in self.t:
        #        value= element + other
        #        copied.append(value)
        #    new_point=tuple(copied)
        #    p=PointND()
        #    p.t=new_point
        #    return p
        #if type(other) == tuple:
        #    p= PointND()
        #    p.t=tuple([item1 + item2 for item1, item2 in zip(other.t, self.t)])
        #    return p

def main():
    p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
    p2 = PointND(0.5, 0.4, 0.3, 0.2, 0.1)
    q = p1 + p2
    print(q.t)
    #print(p1.n)
    #print(p1.t)
    #print(p1.__str__())
    #print(p1.__hash__())
    #print(p1.distanceFrom(p2))

if __name__ == "__main__" :
    main()
