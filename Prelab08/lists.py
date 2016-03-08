#!/usr/bin/env python3
import listmod

if __name__ == "__main__":
    input_a = input("Enter the first list of numbers: ")
    input_b = input("Enter the second list of numbers: ")

    list_1 = [int(x) for x in input_a.split()]
    list_2 = [int(x) for x in input_b.split()]

    print("First list: "+str(list_1))
    print("Second list: "+str(list_2))

    (median_value, final_list) = listmod.find_median(list_1, list_2)
    print("Merged list: "+str(final_list))
    print("Median: "+str(median_value))