# [] * n        -> init by n times
numbers_1 = [3, 7, 8] * 2
print(numbers_1)

# concatenation
numbers_2 = [5, 9, 1]
all_numbers = numbers_1 + numbers_2    # concatenation
print(all_numbers)

# reverse()
all_numbers.reverse()      # reversing order of list.
print("reverse:", all_numbers)
print()

# sorted() -> function that makes a copy in ascending order
my_sorted_numbers = sorted(all_numbers)   # my_sorted_numbers is a copy
print("my_sorted_numbers:", my_sorted_numbers)
print("all_numbers:", all_numbers)

# sort() -> method that modifies the original list (modifies original list)
all_numbers.sort(reverse=True)   # sort in descending order
print("all_numbers after sort(reverse=True):", all_numbers)

# count()
number_of_7s = all_numbers.count(7)
print("Count of 7s:", number_of_7s)

# remove()
all_numbers.remove(7)    # will remove the first instance
print("all_numbers after remove(7):", all_numbers)
print()

# sum() -> total of all numbers
total = sum(all_numbers)
print("total:", total)

numbers_3 = [63, 50, 13, 78, 15, 8, 40]
print("Highest: ", max(numbers_3))   # only apply to unsorted list.
print("Lowest: ", min(numbers_3))    # only apply to unsorted list.
print()
numbers_3.sort()    # sort first
print("Highest: ", numbers_3[-1])    # last item
print("Lowest: ", numbers_3[0])      # first item





