def insertion_sort(lst):
    print(f"The list {lst}")
    print(f"The Unsorted list {lst[1:]}")
    for i in range(1, len(lst)):
        elem_selected = lst[i]
        print(f"Element Selected: {elem_selected}")
        print(f"The swap {lst[i]} = {lst[i - 1]}")
        while i > 0 and elem_selected < lst[i - 1]:
            lst[i] = lst[i - 1]
            # print(f"The swap {lst[i]} = {lst[i - 1]}")
            i -= 1

        lst[i] = elem_selected




insertion_sort([1, 6, 8, 2, 6])