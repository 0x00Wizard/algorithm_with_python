def linear_search(data, item):
    for i in range(len(data)):
        if data[i] == item:
            return i

        return - 1


a = [2, 1, 3, 45, 22, 11, 19]

print(linear_search(a, 45))
