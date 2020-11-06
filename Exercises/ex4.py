autos = 100
espacio_en_el_auto = 4.0
conductores = 30
pasajeros = 90
no_hay_conductores = autos - conductores
autos_conductores = conductores
carnet_conducir = autos_conductores * espacio_en_el_auto
promedio_pasajeros_en_el_auto = pasajeros / autos_conductores


print("Aqui hay" , autos,"promedio de autos.")
print("Solo hay", conductores, "pormedio de conductores.")
print("Puede ser", no_hay_conductores, "no hay autos hoy.")
print("Podemos trasportalos", carnet_conducir, "gente hoy.")
print("Nosotros tenemos", pasajeros, "carnet de conducir hoy.")
print("Necesitamos sobre poner", promedio_pasajeros_en_el_auto, "en cada auto.")
