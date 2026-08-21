seatings = [
    ["Siti", "Chen", "Lim"],       # row 0
    ["Jon", "Kang", "Lee"],        # row 1
    ["Sim", "Ahmad", "Singh"],     # row 2
    ["Lily", "Toto", "Ming"]       # row 3
]   #  0       1       2    col

print("seatings[1][2]:", seatings[1][2])  # Lee
print("seatings[0][0]:", seatings[0][0])  # Siti
print("seatings[-1][-1]:", seatings[-1][-1])   # Ming
print("seatings[3][2]:", seatings[3][2])   # Ming
print("---------------------------------------")

for row in range(len(seatings)):
    # start of row
    for col in range(len(seatings[row])):
        print(f"{seatings[row][col]:12}", end=" ")
    # end of row
    print()