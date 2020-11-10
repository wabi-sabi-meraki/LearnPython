tipos_de_personas = 10
x = f"Aqui hay {tipos_de_personas} tipos_de_personas."

vinario = "vinario"
no_lo_es = "no lo es"
y = f"Sabemos que {vinario} y no lo es {no_lo_es}."

print(x)
print(y)

print(f"Yo digo: {x}")
print(f"Tambien sabemos:'{y}'")

ridiculo = False
evalucion_broma = "Es un acto gracioso! {}"

print(evalucion_broma.format(ridiculo))

w = "Es el lado izquierdo de..."
e = "una cadena del lado derecho."

print(w + e)
