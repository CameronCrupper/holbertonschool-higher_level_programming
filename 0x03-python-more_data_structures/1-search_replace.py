#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for n, i in enumerate(my_list):
        for sublist in my_list:
            if i == search:
                my_list[n]= replace
    print(my_list)