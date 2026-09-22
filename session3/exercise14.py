class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"Name: {self.name}, Email: {self.email}"

user1 = User("Jefferson", "jefferson@gmail.com")
user2 = User("Juan", "juan@gmailcom")
user3 = User("Maria", "maria@gmail.com")
print(user1.display_info())
print(user2.display_info())
print(user3.display_info())

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = 'admin'
    def display_info(self):
        return f"Name: {self.name}, Email: {self.email}, Role: {self.role}"

user4 = Admin("AdminUser", "admin@gmail.com")
user5 = Admin("AdminUser2", "admin2@gmail.com")
print(user4.display_info())
print(user5.display_info())