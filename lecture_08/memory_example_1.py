x = 5.1      # 2482484065264
y = x
print("id of x and x: ", id(x), "->",  x)
print("id of y and y: ", id(y), "->",  y)

y = y - 1.5    # 5 - 1 -> 2482476287216
print("id of y and y: ", id(y), "->",  y)

y = y + 1.5
print("id of y and y: ", id(y), "->", y)