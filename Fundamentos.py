
#Tipo de escritura de variables
nombre = "Brayan Steven"
apellido = "Perez Alarcon"
edad = 18
altura = 1.75
activo = True
correo = "stevnn022007@gmail.com"
telefono = "3113303249"
# se cambia de tipo de dato para que nosotros podamos recibir el dato a otro tipo de dato
telefono_int = int(telefono)
edad_float = float(edad)
altura_int = int(altura)
"""Se llama todas las vraiables cn sus tipos de datos
"""

print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print(type(telefono_int), telefono_int)
print(type(edad_float), edad_float)
print(type(altura_int), altura_int)


# identacion en python

if 5 > 2 :
    print("el numero es mayor que 5")
else:
    print("numero falso")

#ejercicio d practica input:
nombre_completo = input("ingrese su nombre completo: ")

print(nombre_completo)
#se le pide la edad al usuario y despues se imprime pero el dato lo va a tomar de tipo int
edad_persona = int(input("ingrese su edad: "))

#impresion con formato f_string
print(f"hola {nombre_completo}, tienes {edad_persona}")