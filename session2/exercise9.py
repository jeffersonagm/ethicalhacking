def get_valid_age():
    while True:
        try:
            age = int(input("Ingresa tu edad: "))

            if 0 <= age <= 120:
                return age
            else:
                print("La edad debe estar entre 0 y 120.")

        except ValueError:
            print("Error: debes ingresar un número entero.")


edad = get_valid_age()
print(f"Edad válida: {edad}")