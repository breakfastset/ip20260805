# for i in range(start, end, step)
#      statement
# where start and step are optional
#       start defaults to 0
#       step defaults to 1
#       end is excluded
for i in range(3):
    print(i)
# start = 0, end = 3, step = 1
# i -> 0, 1, 2
print("==" * 20)
for i in range(2, 5):
    print(i)
# start = 2, end = 5, step = 1
# i -> 2, 3, 4

print("==" * 20)
for i in range(3, 19, 4):
    print(i)
# start = 3, end = 19, step = 4
# i -> 3, 7, 11, 15

print("==" * 20)
for i in range(5, 0, -1):
    print(i)
print(".....")
# i -> 5, 4, 3, 2, 1




