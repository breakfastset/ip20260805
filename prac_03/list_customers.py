from sys import argv
filename = argv[1]     # read from prog args

in_file = open(filename, "r")
contents = in_file.read()   # read all contents
in_file.close()

print(f"Customers saved in '{filename}': ")
print(contents)