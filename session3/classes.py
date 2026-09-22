class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email

        #print("Usuario creado con éxito.")

    def mostrar_informacion(self):
        return f"name: {self.name}, email: {self.email}"
    

user1 = User("Jefferson", "jefferson@google.com")
user2 = User("Juan", "juan@gmail.com")
user3 = User("Maria", "maria@gmail.com")

#tmp=user1.mostrar_informacion()
#print(tmp)

print(user1.mostrar_informacion())