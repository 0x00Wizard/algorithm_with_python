def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i

        for curr_index in range(i + 1, len(lst)):
            if lst[min_index] > lst[curr_index]:
                min_index = curr_index

        lst[i], lst[min_index] = lst[min_index], lst[i]