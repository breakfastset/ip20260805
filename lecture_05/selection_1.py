# 1. if only

purchase_amount = float(input("Enter purchase amount: "))

if purchase_amount > 500:
    print("You get a 20% discount!")
    purchase_amount = purchase_amount * 0.8

print(f"Please pay ${purchase_amount:.2f}")