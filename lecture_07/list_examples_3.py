# Method 1: Accessing a list using for in loop
#           The variable is a copy of each element
#           in the list.
drinks = ["kopi", "teh", "teh alia", "barley"]
for my_drink in drinks:   # my_drink is a copy
    my_drink = my_drink.upper()
    print(my_drink)
print("Original drinks: ", drinks)  # not modified
print()
# Method 2: Accessing a list using an indexed loop
#           The variable is the actual element
#           in the list.
for i in range(len(drinks)):
    drinks[i] = drinks[i].title()   # actual element
    print(f"{i}: {drinks[i]}")
print("Original drinks: ", drinks)  # Modified
