import math

# Ejercicio 1
#Se declaran las variables nombre, producto, promedio y se imprime las variables en un "fString"
nombre = "Steven"
producto = 20000
promedio = 4.5
print(f"el alumno {nombre} tiene un producto de valor {producto} y un promedio de {promedio}")

# Ejercicio 2
#se declara las variables con un un Input el cual para que ingrese datos de tipo enter
numero1 = int(input("Ingrese un valor entero "))
numero2 = int(input("ingrese un valor entero "))
numero3 = float(input("ingrese valores decimales "))
numero4 = input("ingrese un numero ")
numero5 = input("ingrese el segundo numero ")

# Se hace la operacion de suma de las primeras tres variables
suma = numero1 + numero2 + numero3
print(f"la suma de los numeros es {suma}")
#Se coloca un Max para colocar el limite de mayor de los numeros y se impri,e el munero mayor
numero_mayor = max(numero1, numero2, numero3)
print(f"el numero mayor es {numero_mayor}")

#Se declara la variable division y es igual a la variable numero 3
division = numero3
"""
se le asigna un nuevo valor a division pero en esa misma variable hace una operacion de resto (se hace primero lo del parentesis) 
despues se ejecuta la operacion de la division y se imprime la variable division
"""
division /= (numero1 % numero2)
print(division)
# se declara la variable concatenacion y se suma las vraiables de metodo string
concatenacion = numero4 + numero5
print(concatenacion)  


# ejercicio 3

# se declaran las variables:
base = 5
exponente = 3
# se realiza la operacion de pontenciacion 
potenciacion = base ** exponente
print(f"La potenciacion de base y exponente es: {potenciacion}")

# ejercicio 4
# Se declaran las variables con un input para que el usuario ingrese el dato 
operacion_raiz = int(input("ingresa un numero entero "))
#Se utiliza round para redondear la operacion y se utiliza la Libreria Math.sqrt para sacar la raiz de operacion raiz
raiz = round(math.sqrt(operacion_raiz))

# ejercicio 5
# Se declaran las variables con un input para que el usuario ingrese sus notas.
estudiante = input("Ingrese el nombre del estudiante: ")
decimal1 = float(input("ingrese el valor: "))
decimal2 = float(input("ingrese el valor: "))
decimal3 = float(input("ingrese el valor: "))
decimal4 = float(input("ingrese el valor: "))
decimal5 = float(input("ingrese el valor: "))
# Se declara la variable promedio del estudiante y primero se realiza la operacion de todas las sumas delas notas y ese valor lo divide en el numero de notas.
promedio_estudiante = (decimal1 + decimal2 + decimal3 + decimal4 + decimal5) / 5
print(f"Resultado: {estudiante},{promedio_estudiante}")


# ejercicio 6
#Se declaran las variables:
numeroUno = 8
numeroDos = 2
#Se reasigna un numevo valor a cada variable, (se intercalan)
auxiliar = numeroDos
numeroDos = numeroUno
#se imprime las variables nombradas
print(auxiliar)
print(numeroDos)


# ejercicio 7
estado = False
estado += (5 == 2) or (2 > 1)
print(estado)


#ejercicio 8
#se Crea una variable llamada resultado la cual tiene varias operaciones matematicas
resultado = (9/2) + 8*2/1 -(2+2)
#imprime el resultado
print(resultado )

#Ejercicio 9
#Se crean las variables y se les asigna un valor 
ladoCuadrado = 8
# Se eleva al cuadrado los lados del cuadrado
areaCuadrado = ladoCuadrado ** 2
perimetroCuadrado = 4 * 1
print(f"el lado del cuadrado es {ladoCuadrado}, el are del cuadrado es {areaCuadrado} y el perimetro es {perimetroCuadrado}")

#Se crean las variables
baseTriangulo = 9
alturaTriangulo = 8
ladoTriangulo = 8
ladoDosTriangulo = 8
#se calcula el area del cuadrado
areaTriangulo = (baseTriangulo * alturaTriangulo) /2
#se crea una variable para sumar sus lados para el perimetro
perimetroTriangulo = ladoDosTriangulo + ladoTriangulo + alturaTriangulo
print(f"los lados del triangulo son {alturaTriangulo, ladoTriangulo, ladoDosTriangulo}, el area es: {areaTriangulo} y el perimetro es de : {perimetroCuadrado}")
# Se crea las variables y se crea y se asigna un valor:
baseRectangulo = 8
alturaRectangulo = 6
# Se calcula el area
areaRectangulo = (alturaRectangulo * 2) * (baseRectangulo * 2)
#Se calcula el perimetro
perimetroRectangulo = 2*(alturaRectangulo + baseRectangulo)
print(f"sus lados son {baseRectangulo, alturaRectangulo}, el area es: {areaRectangulo} y su perimero es: {perimetroRectangulo}")


#Ejercicio 10

#Se crea una variable con un input para que el usuario registre su edad 
edadUsuario = int(input("Ingresa un numero entero: "))
# se hace una conmdicion para saber de que edad es.>
if edadUsuario <= 0:
    print("edad no permitida")
else:
    if  edadUsuario <= 5:
        print("Infante")
    elif edadUsuario <= 10:
        print("niño")
    elif edadUsuario <= 15:
        print("pre-adolecente")
    elif edadUsuario <= 18 :
        print("Adolecentes")
    elif edadUsuario <= 25:
        print("pre-adulto")
    elif edadUsuario <= 40:
        print("Adulto")
    elif edadUsuario <= 55:
        print("Pre-Anciono")
    else:
        print("Anciano")
        
        
         
    








