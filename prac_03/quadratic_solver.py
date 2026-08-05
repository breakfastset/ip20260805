a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

determinant = b ** 2 - (4 * a * c)
print("Determinant: ", determinant)

x1 = (b * (-1) + determinant ** 0.5) / (2 * a)
x2 = (b * (-1) - determinant ** 0.5) / (2 * a)

print("x1: ", x1)
print("x2: ", x2)
