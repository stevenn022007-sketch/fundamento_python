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