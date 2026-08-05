# | pipe
row = "| {:10} | {:10} | {:10,.2f} |"    # length: 40
sales_title = " Sales "
top_rule = "{:=^40}"

print(top_rule.format(sales_title))
print(row.format("Oranges", 5, 6.99))
print(row.format("Apples", 2000, 12000))
print(row.format("Bananas", 10, 75))
print("=" * 40)