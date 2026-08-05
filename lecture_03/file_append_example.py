
entry = input("Your thoughts today? ")

out_file = open("diary.txt", "a")
out_file.write(f"{entry}\n")     # \n to ensure a new line
out_file.close()