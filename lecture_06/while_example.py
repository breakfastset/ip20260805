# 1. init variable
# while 2. condition is True for variable
#     3. statements 1
#        ....
#        ....
#     4. alter variable in condition (eventually to False)

count = 0    # 1. init var count
while count < 3:    # 2. while condition is True (count < 3):
    print("Current count is: ", count)  # 3. statement 1
    print("*" * count)   # ...
    count = count + 1   # 4. alter var (such that count >= 3)

print("=out of loop=" * 3)
# 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 -> end