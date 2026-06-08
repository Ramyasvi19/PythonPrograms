departments = {
    "HR": ["Alice", "Bob"],
    "IT": ["Charlie", "David"]
}
for dept, employees in departments.items():
    print(f"Department: {dept}")
    for emp in employees:
        print(f" - {emp}")
        