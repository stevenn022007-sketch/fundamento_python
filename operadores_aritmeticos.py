import math
import random

#Operadores Aritmeticos
a = 5
b = 6

#suma
suma = a + b
print(f"la suma de {a} y {b} es {suma}")

#Resta
resta = a - b 
print(f"La resta de {a} y {b} es {resta}")

#multiplicacion
multiplicacion = a * b 
print(f"la multipliacion de {a} y {b} es de {multiplicacion}")

#division 
division= a / b 
print(f"la division de {a} y {b} es de {division}")

# division entera
division= a // b 
print(f"la division de {a} y {b} es de {division}")

#modulo 
modulo =  a % b
print(f"el residuo de la division de {a} y {b} es de {modulo}")

# Exponenciacion
exponenciacion = a ** b
print(f"la exponenciacion de {a} y {b}")

resultado = a + b * 5
print(f"el resulñtado de la operacion es {resultado}")

resultado2 = (a + b) * 5
print(f"el resulñtado de la operacion es {resultado2}")

#ejrecicio individual
ejercicio = ((a + b)* (a-b) / (a * b) -((a ** b) %3))
print(f"el ejercicio es {ejercicio}")

#librerias


print(math.pi)

random.random()
numero = random.randint(1, 10)
print(numero)

