import timeit

print(timeit.timeit("[i for i in range(10000)]", number=500))


