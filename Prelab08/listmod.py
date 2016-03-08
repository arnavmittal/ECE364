#!/usr/bin/env python3
from math import floor

def find_median(list_a, list_b):
    list_final=[]
    for x in list_a:
        list_final.append(x)
    for x in list_b:
        list_final.append(x)
    list_final.sort()
    mid = floor((len(list_final)-1)/2)
    mid_val = list_final[mid]
    return (mid_val, list_final)
