def partition(i, j, k):
    pass


def quicksort(lst, low, high):
    if low < high:
        pivot_index = partition(lst, low, high)

        quicksort(lst, low, pivot_index-1)
        quicksort(lst, pivot_index + 1, high)
