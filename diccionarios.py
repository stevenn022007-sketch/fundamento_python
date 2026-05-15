#creacion del Diccionario
diccionario = {
    "clave_1": "valor 2",
    "clave_2": "valor 2",
    "clave_3": "valor 2",
}
#un diccionario vacio
diccionario2 = {}

#diccionario con elementos
diccionario_aprendiz ={
    "nombre": "Steven",
    "ficha": "3321349",
    "telefono": "3221122121",
    "edad": 19
}
print(diccionario_aprendiz)
print(type(diccionario_aprendiz))
print(diccionario_aprendiz["telefono"])
print(diccionario_aprendiz.get("ficha"))

#obtener solo las llaves del diccionario
print(diccionario_aprendiz.keys())
#obtener solo los valores del diccionario
print(diccionario_aprendiz.values())
#obtener la llave y el valor 
print(diccionario_aprendiz.items())
#Agregar un elemento al diccionario
diccionario_aprendiz["correo"] = "hdskjfhjskhjkdshs@gmail.com"
print(diccionario_aprendiz)

#modificar datos
diccionario_aprendiz["programa"] = "SST"
print(diccionario_aprendiz)
diccionario_aprendiz["programa"] = "ADSO"
print(diccionario_aprendiz)

#Metodo UPDATE
#actualiza el dato de la llave  
diccionario_aprendiz.update({"nombre": "Andres"})
#agrega el estado porque no existia.
diccionario_aprendiz.update({"Estado": True})
print(diccionario_aprendiz)

#comprobar una dependencia 
if "ficha" in diccionario_aprendiz:
    print("la llave esta dentro del diccionario")
else:
    print("la llave no esta en el diccionario")

#recorrer solo los valores del diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)
#recorrer solo las claves del diccionario
for valor in diccionario_aprendiz.values():
    print(valor)    
    
#recorrer las claves y los valores del diccionario
for clave, valor in diccionario_aprendiz.items():
    print(f"la clave es {clave} y el valor es: {valor}")
    
#eliminar elemnetos en un diccionario
diccionario_aprendiz.popitem() #elimina el ultimo elementoagregado
print(diccionario_aprendiz) 
diccionario_aprendiz.pop("edad")#elimina un elemento especifico o llave especifica
print(diccionario_aprendiz)
diccionario_aprendiz.clear()
print(diccionario_aprendiz)


# Diccionarios Anidados
aprendices = {
    "aprendiz_1": {
        "nombre": "Felipe",
        "apellido": "Sandoval",
        "programa": "ADSO",
        "ficha": "33211349",
        "edad": 32
    },

    "aprendiz_2": {
        "nombre": "Camilo",
        "apellido": "Gomez",
        "programa": "SST",
        "ficha": "33211350",
        "edad": 28
    },

    "aprendiz_3": {
        "nombre": "Valentina",
        "apellido": "Lopez",
        "programa": "Topografia",
        "ficha": "33211351",
        "edad": 25
    }
}

# Acceder a un valor en un Diccionario Anidado
print(aprendices["aprendiz_2"]["programa"])  # SST

for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")