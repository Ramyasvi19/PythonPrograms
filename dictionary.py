employees = [{"id": 1, "name": "Alice", "salary": 50000},
             {"id": 2, "name": "Bob", "salary": 60000},
             {"id": 3, "name": "Charlie", "salary": 55000}]
for employee in employees:
    bonus = employee["salary"] * 0.10
    print(f"{employee['name']} Bonus: {bonus}")

    