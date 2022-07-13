def binary_search(data, item, low, high):
    if low <= high:
        middle = (low + high) // 2

        if data[middle] == item:
            return middle

        elif data[middle] > item:
            return binary_search(data, item, low, middle - 1)

        else:
            return binary_search(data, item, high + 1, high)

    else:
        return -1