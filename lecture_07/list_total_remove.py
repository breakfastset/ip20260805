food = ["chicken rice", "hokkien mee", "nasi lemak", "lontong",
        "hokkien mee", "chilli crab", "pepper crab"]

food_to_remove = "hokkien mee"

while food_to_remove in food:
    food.remove(food_to_remove)

print(food)
print()

numbers = [6, 7, 8, 9, 0, 3, 2, 1, 7, 8, 9, 0, 7, 8]
target = 7
index = 0
while index < len(numbers):
    if numbers[index] == target:
        numbers.pop(index)
    else:
        index += 1
print(numbers)

