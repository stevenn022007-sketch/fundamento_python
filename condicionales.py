#condicionales
if True:
    print("hola mundo")
elif True:
    print("menor")
else:
    print("no mundo")
    
#ejercicio
edad = int(input("ingresa tu edad: "))

if (edad >= 20 and edad < 65):
    print("Adulto")
elif (edad >= 18):
    print("joven")
else:
    print("eres un bebe")    
    
#Anidados

edad2 = int(input("ingresa tu edad: "))

if (edad2 <= 18):
    if(edad2 >= 12 and edad2 <= 18):
        print("Adolecente")
    else:
        print("eres menor")
else:
    if(edad2 > 18):
        if(edad2 > 19 and edad2 < 35):
            print("eres Adulto")
        else:
            print("Adulto mayor")    
        
        
#operador ternario
numero = 4

print("el numero es " if numero % 2 == 0 else print("es impar")) 