def selection_sort(lst):

    for i in range(len(lst)):
        print(f"[+] Outer loop iteration {i}")
        print(f"List {lst}")
        min_index = i
        print(f"Sorted portion {min_index}")
        print(f"The Unsorted portion {lst[:1]}")

        for curr_index in range(i + 1, len(lst)):
            if lst[curr_index] > lst[min_index]:
                lst[curr_index] = min_index



        lst[i], lst[min_index] = lst[min_index], lst[i]