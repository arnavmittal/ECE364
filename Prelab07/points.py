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
        if len(self.t) != len(other.t):
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

    def __add__(self, other):
        if type(other) == float:
            p=PointND()
            p.t=tuple([item1 + other for item1 in self.t])
            return p
        if type(other.t) == tuple:
            if other.n != self.n:
                raise ValueError("Cannot operate on points with different cardinality.")
            p= PointND()
            p.t=tuple([item1 + item2 for item1, item2 in zip(other.t, self.t)])
            return p
    __radd__=__add__

    def __sub__(self, other):
        if type(other) == float:
            p=PointND()
            p.t=tuple([item1 - other for item1 in self.t])
            return p
        if type(other.t) == tuple:
            if other.n != self.n:
                raise ValueError("Cannot operate on points with different cardinality.")
            p= PointND()
            p.t=tuple([item1 - item2 for item1, item2 in zip(self.t, other.t)])
            return p

    def __mul__(self, other):
        if type(other) == float:
            p=PointND()
            p.t=tuple([item1 * other for item1 in self.t])
            return p
        if type(other.t) == tuple:
            if other.n != self.n:
                raise ValueError("Cannot operate on points with different cardinality.")
            p= PointND()
            p.t=tuple([item1 * item2 for item1, item2 in zip(self.t, other.t)])
            return p
    __rmul__=__mul__

    def __truediv__(self, other):
        if type(other) == float:
            p=PointND()
            p.t=tuple([ item1 / other for item1 in self.t])
            return p

        if type(other.t) == tuple:
            if other.n != self.n:
                raise ValueError("Cannot operate on points with different cardinality.")
            p= PointND()
            p.t=tuple([item1 / item2 for item1, item2 in zip(self.t, other.t)])
            return p

    def __neg__(self):
        p = PointND
        p.t=tuple([-item1 for item1 in self.t])
        return p

    def __getitem__(self, item):
        value = self.t[item]
        return value

    def __eq__(self, other):
        if len(other.t) != len(self.t):
            raise ValueError("Cannot operate on points with different cardinality.")
        for element1, element2 in zip(self.t, other.t):
            if element1 != element2:
                return False
        return True

    def __ne__(self, other):
        if len(other.t) != len(self.t):
            raise ValueError("Cannot operate on points with different cardinality.")
        q = self.__eq__(other)
        return not q

    def __gt__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinality.")
        origin = PointND()
        origin.t=tuple([0.0 for item in other.t])
        dist1 = self.distanceFrom(origin)
        dist2 = other.distanceFrom(origin)
        if (dist1 > dist2):
            return True
        return False

    def __ge__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinality.")
        origin = PointND()
        origin.t=tuple([0.0 for item in other.t])
        dist1 = self.distanceFrom(origin)
        dist2 = other.distanceFrom(origin)
        if (dist1 >= dist2):
            return True
        return False

    def __lt__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinality.")
        origin = PointND()
        origin.t=tuple([0.0 for item in other.t])
        dist1 = self.distanceFrom(origin)
        dist2 = other.distanceFrom(origin)
        if (dist1 < dist2):
            return True
        return False

    def __le__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinality.")
        origin = PointND()
        origin.t=tuple([0.0 for item in other.t])
        dist1 = self.distanceFrom(origin)
        dist2 = other.distanceFrom(origin)
        if (dist1 <= dist2):
            return True
        return False

class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        PointND.__init__(self, x, y ,z)


class PointSet:
    def __init__(self, **kwargs):
        new_list=[]
        if len(kwargs) == 0:
            self.points = set()
            self.n=0

        if('pointList' not in kwargs.keys()):
            raise KeyError("'pointList' input parameter not found.")

        if(len(kwargs['pointList'])== 0):
             raise ValueError("'pointList' input parameter cannot be empty.")

        else:
            for element in kwargs['pointList']:
                self.n = kwargs['pointList'][0].n
                if(element.n != self.n):
                    raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
                new_list.append(element)
            self.points=set(new_list)



    def addPoint(self, p):
        if (self.n != p.n):
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        self.points.add(p)

    def count(self):
        return(len(self.points))

    def computeBoundingHyperCube(self):
        max_list=[]
        min_list=[]
        point_max=PointND()
        point_min=PointND()
        for i in range(0,self.n): # checking each component of the point like x, y, z
            max_val= 0.0
            min_val = 10000.0
            for element in self.points: # checking each point for that particular component
                if element[i] > max_val:
                    max_val=element[i]
                if element[i] < min_val:
                    min_val=element[i]
            max_list.append(max_val)
            min_list.append(min_val)
        point_max.t=tuple(max_list)
        point_min.t=tuple(min_list)
        return (point_min, point_max)

    def computeNearestNeighbors(self, otherPointSet):
        new_list=[]
        for point1 in self.points:
            min_dist=100000.0
            for point2 in otherPointSet.points:
                temp_dist = point1.distanceFrom(point2)
                if temp_dist < min_dist:
                    min_dist = temp_dist
                    add_point=point2
            new_list.append((point1, add_point))
        return tuple(new_list)

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        self.points.add(other)
        return self

    def __sub__(self, other):
        if self.n != other.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        self.points.discard(other)
        return self

    def __contains__(self, item):
        for elements in self.points:
            if item == elements:
                return True
        return False

def main():
    p1 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
    p2 = PointND(1.0, 2.1, 3.2, 3.4, 4.5)
    p3 = PointND(1.0, 2.1, 3.2, 5.5)
    q = p1 < p2
    #print(p1.n)
    #print(p1.t)
    #print(p1.__str__())
    #print(p1.__hash__())
    #print(p1.distanceFrom(p2))
    #print(q)

if __name__ == "__main__" :
    main()
