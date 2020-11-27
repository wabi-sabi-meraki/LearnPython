def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return  a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Ahora haremos matematicas con solo funciones!")

edad = add(30, 5)
peso = subtract(60, 10)
altura = multiply(30, 5.5)
iq = divide(100, 2)

print(f"Edad: {edad}, Peso:{peso}, Altura {altura}, IQ {iq}")


# Un rompecabezas por el esfurzo, buen trabajo.
print("Aqui el rompecabezas.")

que = add(edad, subtract(peso, multiply(altura, divide(iq, 2))))

print("Esto comienza: ", que, "Puedes tomar la mano?")
