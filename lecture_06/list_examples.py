animals = ["macaque", "ape","elephant", "okapi", "parrot", "kakapo", "narwhal", "pangolin"]
#             0        1       2           3         4        5          6           7
#           -8        -7      -6          -5       -4        -3         -2          -1

print("first item:", animals[0])       # macaque
print("second item:", animals[1])      # ape
print("last item:", animals[-1])       # pangolin
print("num items:", len(animals))      # 8
# print("IndexError: ", animals[-10])    # IndexError

# Slicing -> take a subset of the list above
part_animals_1 = animals[:4]     # start = 0, end = 4, step = 1 (exclude end)
print(part_animals_1)
part_animals_2 = animals[5:]     # start = 5, end = 8, step = 1 (exclude end)
print(part_animals_2)
part_animals_3 = animals[2:6]    # start = 2, end = 6, step = 1
print(part_animals_3)            # elephant, okapi, parrot, kakapo
part_animals_4 = animals[-3:-7:-1]   # start = -3, end = -7, step = -1
print(part_animals_4)

part_animals_3a = animals[-6:-2]
print(part_animals_3a)

animals_copy = animals[:]     # animals_copy is not the same as animals
reversed_animals_copy = animals[::-1]    # another copy of animals in reverse
print(animals_copy)
print(reversed_animals_copy)
