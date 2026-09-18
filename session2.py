# def saludo():
#     return print("Hola mundo")

# def saludo(nombre):
#     return print(f"Hola, {nombre}!")

# saludo("Jefferson")

# def suma(a,b):
#     if b==0:
#         return print("The second number is zero")
#     else:
#         return print(f"La división de {a} and {b} is {a/b}")

# suma(25,0)

try:
    variable1=int(input("Ingrese un número: "))
except ValueError:
    print("El valor ingresado no es un número válido")
        