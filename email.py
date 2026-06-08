emails=["alice@example.com", "bob@example.com", "invalid_email", "charlie@example.com"]
for email in emails:
    if "@" not in email:
        print(f"{email} is not a valid email address.")