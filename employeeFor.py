employees={
    101: {"name": "ravi", "dept":"IT"},
    102: {"name": "sita", "dept":"HR"},
    103: {"name": "John", "dept":"Finance"}
}
for emp_id, details in employees.items():
    print(emp_id,details["name"], details["dept"])
    