import timeit

NUM_OF_REPETITION = 1000


# Linear Search Algorithm Implementation

def linear_search(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1


# list

a = [i for i in range(10000)]

# First Test - Finding an element at the beginning of the list

test_code_1 = '''
linear_search(a, 50)
'''

