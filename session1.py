#int variable=10
# VARIABLES
# number=10
# name="Jefferson Almeida"
# active=true
# if number>5:
#     print("The number is greater than 5")
# else:
#     print("The number is less than 5")
    
# for i in range(10):
#     print("The number is: ", i)
#     print("The number is: {i}")

# students=list()
# for i in range(100):
#     students.append(i)

# for i in students:
#     print("The student number is: ", i)

# names=["Jefferson", "Agustín", "Carlos", "Juan", "Pedro"]
# for name in names:
#     print(name)

# names={"Jefferson":1, "Agustín":2, "Carlos":3, "Juan":4, "Pedro":5}
# print(names{"Jefferson"})

# for name in names.items():
#     print(name)

estudiantes = [
    {"nombre": "Juan", "calificacion": 8.5},
    {"nombre": "María", "calificacion": 6.2},
    {"nombre": "Pedro", "calificacion": 7.8},
    {"nombre": "Ana", "calificacion": 9.5},
    {"nombre": "Luis", "calificacion": 8.0},
    {"nombre": "Sofía", "calificacion": 9.0},
    {"nombre": "Carlos", "calificacion": 7.5},
    {"nombre": "Valentina", "calificacion": 8.8}
]

for estudiante in estudiantes:
    if estudiante['calificacion'] >= 7.0:
        print(f"El estudiante {estudiante['nombre']} Aprueba")
    else:
        print(f"El estudiante {estudiante['nombre']} Reprueba")
