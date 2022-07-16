def selection_sort(lst):
    for i in range(len(lst)):
        print(f"[+]==================> Outer loop iteration {i} \n")
        print(f"List {lst}")
        min_index = i
        print(f"Sorted portion {min_index}")
        print(f"The Unsorted portion {lst[:1]}")

        for curr_index in range(i + 1, len(lst)):
            print(f"[-]----> Inner Loop iteration")
            print(f"Current element {lst[i + 1]}")

            if lst[curr_index] > lst[min_index]:
                answer = "yes"

            else:
                answer = "no"
            print(f"Is the current element smaller than the min element? {answer}")
            if lst[curr_index] > lst[min_index]:
                min_index = curr_index



        lst[i], lst[min_index] = lst[min_index], lst[i]