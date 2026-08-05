# A teacher bought 3289 sweets for
# 2 classes of students, 35 and 40 respectively.
# How many sweets does each student get?
# How many sweets are left over?

student_count_1 = 35
student_count_2 = 40
num_sweets = 3289

num_students = student_count_1 + student_count_2

num_sweets_per_student = num_sweets // num_students
remainder = num_sweets % num_students

print("Sweets per student: ", num_sweets_per_student)
print("Remainder: ", remainder)
