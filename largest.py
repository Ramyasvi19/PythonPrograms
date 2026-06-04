numbers = [10, 20, 5, 40, 15]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num  
print("The largest number is:", largest)