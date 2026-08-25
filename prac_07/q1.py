FILENAME = "numbers.csv"

in_file = open(FILENAME, "r")

# 1. for each line
#   2. convert the line into a list of integers
#   filter the list integers into another sorted list each element >= 10
#   print the new list contents delimited with comma ,

# 1.
for line in in_file:
    numbers = line.split(",")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])   # 2.
    filtered_numbers = [x for x in numbers if x >= 10]
    filtered_numbers.sort()     # 3.
    print(*filtered_numbers, sep=",")   # 4.

in_file.close()