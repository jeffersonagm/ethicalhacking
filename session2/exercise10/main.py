from utils import is_valid_email

email = input("Introduce tu correo: ")

if is_valid_email(email):
    print("Correo válido")
else:
    print("Correo no válido")