#se crea una Array el cual contiene varios datos de personas
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "activo": True},
    {"nombre": "Luis", "edad": 30, "ciudad": "Bogotá", "activo": True},
    {"nombre": "Marta", "edad": 22, "ciudad": "Ciudad de México", "activo": False}
]
#el Usuario puede ingresar el nombre del usuario al que quiera buscar
name_user = input("ingresa el nombre de la persona que quieras buscar: ")
"""
Aca El sistema valida que el nombre de usuario esta en la base de datos si no imprime "ese suaurio no existe en la base de datos"
"""
if personas[0]["nombre"] == name_user  and personas[0]["activo"]:
    print(f"Buscas a : {personas[0]}")

else:
    if personas[1]["nombre"] == name_user  and personas[1]["activo"]:
        print(f"buscas a {personas[1]}")
    elif personas[2]["nombre"] == name_user  and personas[2]["activo"]:
        print(f"buscas a {personas[2]}")
    else:
        print("ese usuario no existe en la base de datos")
 
    

