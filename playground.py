def insertion_sort(lst):
    for i in range(len(lst)):
        elem_selected = lst[i]

        while i > 0 and elem_selected < lst[i - 1]:
            lst[i] = lst[i - 1]
            i -= 1

        lst[i] = elem_selected
