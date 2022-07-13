def linear_search(main_list, item):
    print("Starting Linear Search Algorithm")
    for i in range(len(main_list)):
        print(f"============ Iteration #{i} ============")
        print("Current list item:", main_list[i])
        print("Item searched:", item)
        print("Is the current item equal to the item searched?", main_list[i] == item)
        if main_list[i] == item:
            print(f"Item found! at index {i}")
            return i
        print("This is not the item")
    print("The item is not in the list")
    return -1


linear_search([1, 2, 4, 5, 2, 22, 12, 18, 43, 10], 12)
