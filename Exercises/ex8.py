formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("uno" , "dos" , "tres" , "cuatro"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Trata",
    "Poner un texto aqui",
    "Talvez un poema",
    "O una cancion de amor"
))
