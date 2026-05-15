#listas

#Esrtuctura de una arrays
# indice es el posicionamiento de los datos dentro el array.

listas = ["alarcon", 2, True ]
print(listas[1 ])
#Crear una lista vacia
aprendicces = ["sara","steven", "sofia", "ronalt", "pepa"]
print(aprendicces[0]) # un solo dato y es "Sara".

#modificar datos
aprendicces[2] = "Sonia"
print(aprendicces)

nombre ="steven"
edad = 20

lista = [nombre, edad]
print(lista)
nombre = "STEVEN"
print(lista)

#consultar rangos de la lista
print(aprendicces[1:2])# NO TRAE EL DATO 2 LOS : ES PARA UN RANGO
print(aprendicces[1::3])
print(aprendicces[2:5])


#SUMA DE ARRAY
lista1 = ["pepe", 25]
lista2 = ["SOFIA", 30]
lista3 = lista1 + lista2
print(lista3) 

vocales = ["a","e","i","o"]
print(vocales)
vocales += ["u"]
print(vocales)

#unir listas con Extend

aprendices123456 = ["andres","luis","ronalt","simon"]
aprendices1234567 = ["Steven","andres","julian",]

aprendices123456.extend(aprendices1234567)
print(f"LOS APRENDICES SON {aprendices123456}")

#medir el largo con len()

print(len(aprendices123456))

# contar elementos con count()
count_aprendices = aprendices123456.count("andres")
print(f"el nombre que se repite mas es {count_aprendices}")

# saber que posicion es index()
index_poscision = aprendices1234567.index("julian")
print(f"el pocisionamiento de julian es de {index_poscision}")

#copiar una lista dentro de otra variable 
x = aprendices1234567.copy()
print(f"la de copia es {x}")

#agregar elementos append()
agregar_aprendiz = aprendices1234567.append("sofia")
print(f"se garego a sofia {agregar_aprendiz} {aprendices1234567}")

# agregar en cualquier indice insert()
aprendices1234567.insert(3, "James") 
print(aprendices1234567)

#eliminar elementos por valor remove()
aprendices1234567.remove("James")
print(aprendices1234567)
#eliminar elementos por el indice pop()
aprendices1234567.pop(0)
print(aprendices1234567)

#comprobar pertenencia in()
if "james" in aprendices1234567:
    print("james esta en la lista ehorabuena")
else:
    print("james no esta en la lista")
    
#ordenar lista alfabeticamnete sort()
aprendices1234567.sort()
print(aprendices1234567)
#ordenar de forma decendente reverce()
aprendices1234567.reverse()
print(aprendices1234567)
# eliminar los elementos de la lista
aprendices1234567.clear()
print(aprendices1234567)