# and   -> all conditions must be True
# or    -> at least one condition is True
# not   -> flip the logic

is_uob_customer = False
num_points = 15_000
can_attend_concert = (is_uob_customer == True and num_points >= 10_000)
print(can_attend_concert)
# if the first condition is found to be False in an 'and' clause
#    there is no need to check other conditions
# -> short-circuiting
print()

grade_points = 4
activity_achievement = 'national'

admission_success = (grade_points <= 5 or activity_achievement == 'national')
print(admission_success)    # True
# if the first condition is found to be True in an 'or' clause
#    there is no need to check other conditions
# -> short-circuiting

print()
is_happy = True
sales = 50_000    # 50_000 is the same as 50000   (int)
print(not is_happy)     # False   ->  not True
print(not (sales < 10_000))   # True  ->    not (50_000 < 10_000) = not False

