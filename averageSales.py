sales = [1000, 1500, 2000, 2500, 3000]
total = 0
for sale in sales:
    total += sale
average = total / len(sales)
print("Average sales:", average)
print("Total sales:", total)
