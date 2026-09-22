class User:
    def __init__(self, port, status):
        self.port = port
        self.status = status

    def display_info(self):
        port_status = "Abierto" if self.status else "Cerrado"
        return f"Puerto: {self.port}, Estado: {port_status}"


user1 = User(80, True)
user2 = User(22, False)

print(user1.display_info())
print(user2.display_info())
