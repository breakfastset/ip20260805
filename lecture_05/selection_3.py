# 3. if .. .elif .. .elif .... else
score = float(input("Enter your score: "))

if 80 <= score <= 100:
    grade = "A"
elif 70 <= score < 80:
    grade = "B"
elif 60 <= score < 70:
    grade = "C"
elif 50 <= score < 60:
    grade = "D"
elif 40 <= score < 50:
    grade = "P"
elif 0 <= score < 40:
    grade = "F"
else:
    grade = "U"      # Ungraded

print(f"You get {grade} for score of {score}.")
