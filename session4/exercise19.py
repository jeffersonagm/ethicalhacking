def find_user_by_email(users, email):
    return next(
        (user for user in users if user["email"] == email),
        None
    )


users = [
    {"name": "Jefferson", "email": "jefferson@gmail.com"},
    {"name": "Carlos", "email": "carlos@gmail.com"},
    {"name": "Ana", "email": "ana@gmail.com"}
]

user = find_user_by_email(users, "carlos@gmail.com")

print(user)