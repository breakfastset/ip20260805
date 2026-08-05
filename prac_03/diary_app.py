diary_filename = "diary.txt"

# 1. read 1 line from diary.txt and display
#
in_file = open(diary_filename, "r")
last_entry = in_file.readline()
# in_file.seek(0)              # go back to start and
# contents = in_file.read()    # read all contents -> meant for appending
in_file.close()

print("Your last entry is: ", last_entry)

# 2. ask the user for diary entry today
#
new_entry = input("Your thoughts for today? ")

# 3. save the new diary entry and all other entries to the diary.txt
#
out_file = open(diary_filename, "w")
# out_file.write(new_entry + "\n" + contents)   # new entry at the top, old entries at the bottom
out_file.seek(0)
out_file.write(new_entry + "\n")
out_file.close()
