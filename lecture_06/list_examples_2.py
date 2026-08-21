fruits = ["rambutan", "lychee", "durian", "mango", "mangosteen"]

fruits.append("longan")   # add to the back of the list
print(fruits)

fruits.pop()    # remove last item
print(fruits)

fruits.pop(3)   # remove item at index 3
print(fruits)

fruits.insert(1, "soursop")   # insert item at position 1
print(fruits)

print("-" * 40)

my_drink = "Ice Mountain Drinking Water"
print(my_drink)
chars = list(my_drink)      # converts string into a list of all chars
print(chars)
words = my_drink.split()    # converts string into a list of words separated by white space
print(words)

print("-" * 40)
print("Water" in words)     # True
print("water" in words)     # False
for word in words:
    print(word.upper())
print(words)                # does not affect original list




