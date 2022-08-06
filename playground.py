import random

a = [i for i in range(1000)]

random.shuffle(a)


def partition(lst, low, high):
    pivot = lst[high]

    i = low - 1

    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[high] = lst[i + 1], lst[high]
    return i + 1


def quicksort(lst, low, high):

    if low < high:
        pivot_index = partition(lst, low, high)

        partition(lst, low, pivot_index - 1)
        partition(lst, pivot_index - 1, high)