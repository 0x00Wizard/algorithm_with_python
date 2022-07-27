# Write your code below this line
# Define a fuction name sort_client
# def sort_client(lst):
#     for i in range(1, len(lst)):
#         elem_selected = lst[i]
#
#         while i > 0 and elem_selected < lst[i - 1]:
#             lst[i] = lst[i - 1]
#             i -= 1
#
#         lst[i] = elem_selected
#
# Define a sort_clients function that takes a list as a parameter.
#
# The list contains tuples. The structure of each tuple is: (<client_name>, <current_balance>) where client_name is a
# string and current_balance is an integer (for this exercise, you can assume that the balances are integers).
#
# Example: [("Nora", 20000), ("Gino", 500), ("Danny", 152), ("William", 10000)]
#
# The function must implement the Insertion Sort algorithm to sort the clients in ascending order, according to their
# current balance.
#
# Your function must return a tuple with the following elements (in this exact order):
#
#     The number of assignments performed (number of iterations of the for loop).
#
#     The number of iterations of the inner (while) loop.
#
#     The name of the client with the greatest balance.


def sort_client(lst):
    num_swaps = 0
    num_iter_inner_loop = 0

    for i in range(1, len(lst)):
        elem_selected = lst[i]

        while i > 0 and elem_selected[1] < lst[i - 1][1]:
            num_iter_inner_loop += 1
            lst[i] = lst[i - 1]

        lst[i] = elem_selected
        num_swaps += 1

    return (num_swaps, num_iter_inner_loop, lst[-1][0])


a = [("Nora", 20000), ("Gino", 500), ("Danny", 152), ("William", 10000)]

print(sort_client(a))
