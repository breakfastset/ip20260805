# all lists will be of size n where n is a big number

def print_last(items):
    """Print the last item in a list of size n."""
    print(items[-1])    # 1
    # Step count = 1, Complexity is O(1)

def add_next_3_consecutive_numbers(n):
    """n is an integer."""
    total = n                     # 1
    total = total + n + 1         # 1
    total = total + n + 2         # 1
    return total                  # 1
    # Total steps = 4, Complexity is O(4) -> O(1)

def print_all_in_list(a_list):
    """Print the entire list item by item in an indexed format."""
    print("All items in the list: ")   # 1
    for i in range(len(a_list)):       # n
        print(f"{i:2}) {a_list[i]}")   # n
    print("---- End of list ----")     # 1
    # Total steps = 2n + 2,  Complexity is O(2n + 2) -> O(n)
    # O(2n + 2) -> O(2n)   take only the highest order
    #           -> O(n)    ignore coefficients

def print_list_of_lists(list_of_lists):
    """Print all lists and their items in an indexed format."""
    print("---- Printing list of lists ---- ")       # 1
    for row in range(len(list_of_lists)):            # n
        print("-> New row")                          # n
        for col in range(len(list_of_lists[row])):   # n * n
            print("({}, {}) {}".format(row, col, list_of_lists[row][col]))  # n * n
    # Assumption is that each inner list is of size n
    # The outer list is of size n
    # Total steps = 2n^2 + 2n + 1
    # O(2n^2 + 2n + 1) -> O(2n^2)    take only the highest order
    #                  -> O(n^2)     ignore the coefficient



my_list_of_lists = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]
print_list_of_lists(my_list_of_lists)