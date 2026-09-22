def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


try:
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} °C = {fahrenheit:.2f} °F")

    fahrenheit_input = float(input("Ingresa la temperatura en Fahrenheit: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit_input)
    print(f"{fahrenheit_input} °F = {celsius_result:.2f} °C")

except ValueError:
    print("Error: debes ingresar un número.")