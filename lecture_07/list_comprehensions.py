# Collect squares of all numbers from 1 to 8
# Method 1: Normal loop
squares = []
for i in range(1, 9):
    squares.append(i ** 2)
print(squares)

print()
# Method 2: List comprehension
squares_2 = [x ** 2 for x in range(1, 9)]
print(squares_2)
print()

###########################################
ones = []
for i in range(5):
    ones.append("ONE")   # Collect "ONE"
print(ones)
print()

#         TO_COLLECT for x in range ...
ones_2 = ["ONE" for x in range(5)]
print(ones_2)
print()

##################################
# Normal Loop
#################################
text = "hours and minutes"
vowels = []
for char in text:
    if char in "aeiou":
        vowels.append(char)
print(vowels)
print()

# List Comprehension version
vowels_2 = [char for char in text if char in "aeiou"]
print(vowels_2)
print("------------------------")

########################################
# Normal Loop
# Get a list with even numbers only.
# If the even number > 50, represent with BIG
# otherwise represent with SMALL
#######################################
numbers = [67, 89, 50, 70, 20, 22, 45, 66, 43, 44]
even_labels = []
for num in numbers:
    if num % 2 == 0:    # even number
        if num > 50:
            even_labels.append("BIG")
        else:
            even_labels.append("SMALL")
print(even_labels)
print()

# List comprehension version
even_labels_2 = ["BIG" if num > 50 else "SMALL" for num in numbers if num % 2 == 0]
print(even_labels_2)



