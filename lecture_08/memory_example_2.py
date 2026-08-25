drinks = ["coffee", "tea", "milo", "milk", "bandung"]

drinks_2 = drinks

print(f"  id of drinks: {id(drinks)}")
print(f"id of drinks_2: {id(drinks_2)}")

drinks[-1] = "chocolate"
print("   drinks: ", drinks)
print(" drinks_2: ", drinks_2)

# drinks 3, 4, 5, 6 are copies
drinks_3 = list(drinks)
drinks_4 = drinks[:]
drinks_5 = [x for x in drinks]
drinks_6 = drinks.copy()

drinks_3[0] = "viet coffee"
drinks_4[-1] = "durian"
drinks_5[1] = "pu er"
drinks_6[3] = "soya"
print()

print("  drinks: ", drinks)
print("drinks_2: ", drinks_2)
print("drinks_3: ", drinks_3)
print("drinks_4: ", drinks_4)
print("drinks_5: ", drinks_5)
print("drinks_6: ", drinks_6)


