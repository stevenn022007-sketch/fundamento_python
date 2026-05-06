# Se declaran las variables pára realizar las operaciones 
estatura = float(input("ingresa tu estatura: "))
peso = float(input("ingresa tu peso: "))
#Se realiza la operacion de la masa corporal y se redondea a 2 decimales y guarda el dato.
masa_corporal = round(peso / (estatura **2 ), 2)
 
"""
hacemos un anidado el cual el primer if contiene que:
que si la estatura o el peso son menores o iguales a 0 imprime "Ingresa un valor positivo"
si no sigue al siguiente procedimiento del anidado.
"""
if(estatura <= 0 or peso <= 0 ):
    print("ingresa un valor positivo")
else:
    if(masa_corporal < 18.5):
        print(f"Su indice de masa corporal es de {masa_corporal}")
        print(f"El usuario tiene una estatura: {estatura} y tiene un peso {peso}, Clasificado como: Bajo")

    elif(masa_corporal <= 18.5 or peso >= 24.9):
        print(f"Su indice de masa corporal es de {masa_corporal}")
        print(f"El usuario tiene una estatura: {estatura} y tiene un peso {peso}, Clasificado como: Normal")
    elif(masa_corporal <= 25 or peso <= 29.9):
        print(f"Su indice de masa corporal es de {masa_corporal}")
        print(f"El usuario tiene una estatura: {estatura} y tiene un peso {peso}, Clasificado como: Sobrepeso")
    else:
        print(f"Su indice de masa corporal es de {masa_corporal}")
        print(f"El usuario tiene una estatura: {estatura} y tiene un peso {peso}, Clasificado como: obesidad")