def linear_search(main_list, item):
    for i in range(len(main_list)):
        if main_list[item] == item:
            return i

    return -1
