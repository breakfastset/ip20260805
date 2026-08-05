out_file = open("my_list.txt", "w")   # open for writing
out_file.write("chilli\n")
out_file.write("ginger\n")
out_file.write("vinegar\n")
out_file.close()    # always remember to close the file

# w mode will create a new file if not found
# w mode will overwrite the contents if the file exists
try:
    pass
except Exception as e:
    pass