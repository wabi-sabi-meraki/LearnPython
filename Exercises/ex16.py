from sys import argv

script, archivo = argv

print(f"Vamos a borrar {archivo}.")
print("Si tu no lo quieres, hit CTRL-C(^C).")
print("Si tu lo quieres hacer, hit RETURN.")

input("?")

print("Abriendo el archivo...")
target = open(archivo, 'w')

print("Truncating el archivo. Adios!")
target.truncate()

print("Ahora yo voy hacerte unas lineas.")

linea1 = input("linea 1:")
linea2 = input("linea 2:")
linea3 = input("linea 3:")

print("Voy a escribir esto en mi archivo.")

target.write(linea1)
target.write("\n")
target.write(linea2)
target.write("\n")
target.write(linea3)
target.write("\n")

print("y finalmente, vamos a cerrar.")
target.close()
