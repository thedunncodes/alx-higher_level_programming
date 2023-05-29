#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            count += 1
        if not (x > count):
            for p in range(x):
                print(my_list[p], end="")
            print()
            return x
        else:
            for i in range(count):
                print(my_list[i], end="")
            print()
            return (count)
    except IndexError:
        print("Error...")
