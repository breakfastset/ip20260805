in_file = open("quotes.txt", "r")    # open file for reading, in_file is file object

four_chars = in_file.read(4)
print("four_chars: ", four_chars)  # Life
rest_of_line = in_file.readline()   # read until end of line
print("rest_of_line: ", rest_of_line)  #  is not just ....

print("Current position in file: ", in_file.tell())  # how many chars read
second_line = in_file.readline()
third_line = in_file.readline()
print("second_line: ", second_line)
print("third_line: ", third_line)

rest_of_the_file = in_file.read()    # reading everything else
print("=" * 40)
print("rest_of_the_file: ", rest_of_the_file)

more_chars = in_file.read(1000)     # read past the end of file
print(f"more_chars: [{more_chars}]")  # empty string

print("-" * 40)
in_file.seek(0)     # go back to the start of the file
lines = in_file.readlines()    # read all lines into a list of strings
print(lines)    # print a list of all lines in the file

in_file.close()   # always remember to close the file