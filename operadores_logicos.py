#operadores logicos
#AND

print(False and False)
print(False and True)
print(True and False)
print(True and True)
#OR
print(False or False)
print(False or True)
print(True or False)
print(True or True)
#NOT
print(not True)
print(not False)

ejercicio = (5 < 3 and 2 > 4)
print(f"el valor es {ejercicio}")
ejercicio = (5 < 3 and 2 < 4)
print(f"el valor es {ejercicio}")
ejercicio = (5 > 3 and 2 > 4)
print(f"el valor es {ejercicio}")
ejercicio = (5 > 3 and 2 < 4)
print(f"el valor es {ejercicio}")

ejercicio2 = (5 < 3 or 2 > 4)
print(f"el valor es {ejercicio2}")
ejercicio2 = (5 < 3 or 2 < 4)
print(f"el valor es {ejercicio2}")
ejercicio2 = (5 > 3 or 2 > 4)
print(f"el valor es {ejercicio2}")
ejercicio2 = (5 > 3 or 2 < 4)
print(f"el valor es {ejercicio2}")

ejercicio3 = (not 5 > 2) or (not 2 < 1)
print(f"el ejercicio n3 es {ejercicio3}")




