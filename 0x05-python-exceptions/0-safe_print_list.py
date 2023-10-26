#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    int count = 0
    for i in my_list:
        if count == x :
            break
        try:
            print(my_list[i]), end ="")
            count +=1
        except (IndexError):
            pass
    print("")
    return count
