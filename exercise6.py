users = [
    {"name": "Ana", "role": "admin"},
    {"name": "Luis", "role": "user"},
    {"name": "Pedro", "role": "admin"},
    {"name": "Sofía", "role": "editor"},
]

roles = []

for user in users:
    if user["role"] not in roles:
        roles.append(user["role"])

print(roles)