class User:
    user_count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.user_count += 1

    def display(self):
        print(f"Nombre: {self.name} | Email: {self.email}")


users = [
    User("Jefferson", "jefferson@gmail.com"),
    User("Carlos", "carlos@gmail.com"),
    User("Ana", "ana@gmail.com")
]

for user in users:
    user.display()

print(f"Usuarios creados: {User.user_count}")