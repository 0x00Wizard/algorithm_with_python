def binary_search(data, item):
    print(data)
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2

        if data[middle] == item:
            return middle

        elif data[middle] > item:
            high = middle - 1

        else:
            low = middle + 1

    return -1


print(binary_search([x for x in range(0, 500000, 2)], 56252))
