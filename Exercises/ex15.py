from sys import argv

script, archivo = argv

txt = open(archivo)

print(f"Aqui tu archvo {archivo}:")
print(txt)

print("Tipo de archivo otravez:")
archivo_otravez = input("> ")

txt_otravez = open(archivo_otravez)

print(txt_otravez.read())
