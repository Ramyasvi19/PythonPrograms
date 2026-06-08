trasactions = [{"id": 101, "amount": 500}, 
                {"id": 102, "amount": 1500}, 
                {"id": 103, "amount": 2000},
                {"id": 104, "amount": 2500}]
balance = 0
for txn in trasactions:
    balance += txn["amount"]
print("Total balance:", balance)    