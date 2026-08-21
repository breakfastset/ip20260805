# a while loop is normally used for unknown number of executions
# a for loop is used for known number of executions

total = 0
num_scores = 0
score = float(input("Enter a score: "))  # 1. init
while 0 <= score <= 100:   # 2. while condition is True
    total += score      # 3. add current score to total
    num_scores += 1     # 3. increase count by 1
    print(f"Total so far: {total} for {num_scores} scores.") # 3.
    score = float(input("Enter another score: "))   # 4. alter var

if num_scores > 0:
    average = total / num_scores
    print(f"Average score: {average} for {num_scores} scores.")
else:
    print("No scores entered.")
