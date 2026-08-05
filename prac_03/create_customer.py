from sys import argv

filename = argv[1]    # take from prog args
customer_name = input("Customer name? ")
customer_id = input("Customer ID? ")

line = f"{customer_name} {customer_id}\n"

out_file = open(filename, "a")   # add to the file
out_file.write(line)
out_file.close()

