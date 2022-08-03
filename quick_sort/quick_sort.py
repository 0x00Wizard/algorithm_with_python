def partition(lst, low, high):
    pivot = lst[high]

    i = low - 1

    for j in range(lst, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst