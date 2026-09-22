productos = [
    {"item": "Pan", "price": 1.50},
    {"item": "Leche", "price": 2.00},
    {"item": "Arroz", "price": 3.00}
]
total = 0
for producto in productos:
    total += producto["price"]
print("El total de la compra es: $", total)