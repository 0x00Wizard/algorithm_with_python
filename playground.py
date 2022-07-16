def bubble_sort(lst):
    print(f"List {lst}")
    n = len(lst)
    print(f"Length of list {n}")
    for i in range(n):
        print("=" * 50)
        print(f"index of the outer-loop {i} \n")
        swapped = False

        for j in range(0, n - i - 1):
            calculation = n - i - 1
            print(f"{n} - {i} - 1 = {calculation}")
            print(f"index of the inner loop {j} \n")
            print(f"List {lst}")
            print(f"first index {j} = {lst[j]} \n")
            print(f"Second index {j + 1} = {lst[j + 1]} \n")

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(f"list {lst} \n")
                print(f"Yes {lst[j]} > {lst[j + 1]} \n")
                swapped = True

        if not swapped:
            break


print(bubble_sort([6, 2, 3, 5, 1, 4, 9, 8]))
