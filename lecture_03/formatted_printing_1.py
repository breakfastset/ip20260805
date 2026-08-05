# d, e, f
a = 3
b = 4
c = 5

# 1. number formatting
print("a: {0:d}, {0:f}, {0:.2f}, {0:e},".format(a))

# 2. position formatting
print("{}, {}, {}".format(a, b, c))   # 3, 4, 5
print("{0}, {1}, {2}".format(a, b, c))   # 3, 4, 5
#                            0  1  2
print("{2}, {1}, {0}".format(a, b, c))   # 5, 3, 4

# 3. length formatting  ->     10 spaces,     10 spaces with 5 decimal points
print("|{0:10}|, |{1:10.5f}|".format(a, b))  # |         3|, |   4.00000|
# 4.00000 takes up 7 spaces

# 4. alignment     left <  right >  center ^
# => strings align to the left by default
# => numbers align to the right by default
quantity = 123
product = "Bottle"
print("|{:20}|{:20}|".format(product, quantity))  # |Bottle              |                 123|
print("|{:>20}|{:<20}|".format(product, quantity)) # |              Bottle|123                 |
print("|{:^20}|{:^20}|".format(product, quantity)) # |       Bottle       |        123         |

# 5. fillers for empty spaces
my_title = "Products"
print("|{:^30}|".format(my_title))
print("|{:+^30}|".format(my_title))
print("|{:0^30}|".format(my_title))






