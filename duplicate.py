numbers = [10, 20, 5, 40, 15,5, 10,45]
seen = set()
for num in numbers:
    if num in seen:
        print("Duplicate found:", num)
    else:
        seen.add(num)   