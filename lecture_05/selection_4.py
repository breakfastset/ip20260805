# 4. nested ifs else
#    when you test for 2 or more conditions
#
# if above 21 and working -> 200
# if above 21 and not working -> 400
# if above 65 and working -> 500
# if above 65 and not working -> 850

# Example 1: NOT using nested ifs
age = 70
working = False
government_payout = 0

if age > 65 and working:
    government_payout = 500
elif age > 65 and not working:
    government_payout = 850
elif age > 21 and working:
    government_payout = 200
elif age > 21 and not working:
    government_payout = 400

print(f"You get ${government_payout}")
print("-=" * 20)

if age > 65:
    if working:
        government_payout = 500
    else:
        government_payout = 850
elif age > 21:
    if working:
        government_payout = 200
    else:
        government_payout = 400

print(f"You get ${government_payout} !!!")

