user = list()
user.append({"name": "Jefferson", "email": "jefferson@gmail.com", "role": "user"})
user.append({"name": "Juan", "email": "juan@gmail.com", "role": "user"})
user.append({"name": "Maria", "email": "maria@gmail.com", "role": "user"})
user.append({"name": "AdminUser", "email": "admin@gmail.com", "role": "admin"})

counter=list()

for u in user:
    if u["role"]=="admin":
        print(f"Name: {u['name']}, Email: {u['email']}, Role: {u['role']}")
        counter.append(u)

print(f"Total Admin Users: {len(counter)}")