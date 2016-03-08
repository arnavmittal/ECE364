#!/usr/bin/env python3

if __name__ == "__main__":
    input_1 = input("Please enter some values: ")

    list_1 = input_1.split()
    t_sum = 0.0
    for x in list_1:
        try:
            t_sum += float(x)
        except ValueError:
            pass

    print("The sum is: {}".format(t_sum))