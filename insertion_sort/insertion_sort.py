def insertion_sort(lst):
    print("=====================> Starting Insertion Sort")
    for i in range(1, len(lst)):
        print(f"---> Outer loop. Iteration #{i}")
        print(f"Sorted Portion: {lst[i - 1]}")
        print(f"Unsorted portion: {lst[1:]}")
        print(f"We need to find the correct spot for: {lst[i]}")
        print(f"{lst[i]} is the first element in the unsorted portion")
        print("Let's find where it belongs...")
        elem_selected = lst[i]

        while i > 0 and elem_selected < lst[i - 1]:
            print()
            lst[i] = lst[i - 1]
            i -= 1

        lst[i] = elem_selected


print(insertion_sort([6, 1, 8, 2, 6]))
