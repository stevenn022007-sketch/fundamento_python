#operadores aritmeticos
a = float(input("ingrese un numero: "))
b = float(input("ingrese el segundo numero :"))
tipo_operacion = input("1. suma 2. resta 3.multipliacion 4.division ")

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

if tipo_operacion == "suma":
    print(f"el resultado es {suma}")
elif tipo_operacion == "resta":
    print(f"el resultado es {resta}")
elif tipo_operacion == "multiplicacion":
    print(f"el resultado es {multiplicacion}")
elif tipo_operacion == "division":
    print(f"el resultado es {division}")
else: 
    print("dato incorrecto")    

        
        
    


