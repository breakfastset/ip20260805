name = "Kuando"
age = 20
gpa = 3.68

# Student Kuando, 20yo, scores 3.68 for GPA.

# Method 1: using +
print("Student " + name + ", " + str(age) + "yo, scores " + str(gpa) + " for GPA.")

# Method 2: using ,
print("Student ", name, ", " , age, "yo, scores ", gpa, " for GPA.", sep="")

# Method 3: using .format
print("Student {}, {}yo, scores {} for GPA.".format(name, age, gpa))

# Method 4: using print f (formatted string)
print(f"Student {name}, {age}yo, scores {gpa} for GPA.")