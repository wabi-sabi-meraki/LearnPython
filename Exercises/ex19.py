def avena_y_platanos(avena_count, cajas_de_platanos):
    print(f"Tu tienes {avena_count} avena!")
    print(f"Tu tienes {cajas_de_platanos} cajas_de_platanos!")
    print("Tendremos un rico desayuno!")
    print("Obtendremos un blanket.\n")


print("Nosotros tendremos la function numbers directly:")
avena_y_platanos(20, 30)


print("O, nosotros podemos usar varibales de nuestro script")
amount_of_avena = 10
amount_of_platanos = 50

avena_y_platanos(amount_of_avena, amount_of_platanos)


print("Nosotros podemos usar las matematicas inside too:")
avena_y_platanos(10 + 20, 5 + 6)


print("Y nosotros podemos combinar los dos, varaibales y matematicas:")
avena_y_platanos(amount_of_avena + 100, amount_of_platanos + 1000)           
