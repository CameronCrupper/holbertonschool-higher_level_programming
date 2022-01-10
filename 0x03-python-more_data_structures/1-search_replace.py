#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for item in my_list:
        if type(item) == list:
            result.append(search_replace(item, search, replace))
        elif item == search:
            result.append(replace)
        else:
            result.append(item)
    return result