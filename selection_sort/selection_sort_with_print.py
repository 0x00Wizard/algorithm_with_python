def selection_sort(lst):
    for i in range(len(lst)):
        print(f"[+]==================> Outer loop iteration {i} \n")
        print(f"List {lst}")
        min_index = i
        print(f"Sorted portion {min_index}")
        print(f"The Unsorted portion {lst[1:]} \n")

        for curr_index in range(i + 1, len(lst)):
            print(f"[-]----> Inner Loop iteration")
            print(f"Current element: {lst[curr_index]}")
            print(f"Min element so far: {lst[min_index]}")

            if lst[curr_index] > lst[min_index]:
                answer = "yes"
                print(f"Is the current element smaller than the min element? {answer}")
                min_index = curr_index
                print(f"{lst[curr_index]} is now the new min element. It is located at index: {min_index} \n")
            else:
                answer = "no"
                print(f"Is the current element smaller than the min element? {answer}")
                print("No need to change the min element \n")

        lst[i], lst[min_index] = lst[min_index], lst[i]


selection_sort([6, 2, 3, 5, 1, 4, 9, 8])
