# se crea una variable de tipo list el cual almacena datos de temperaturas por 14 dias
temperaturas= [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]
#se imprime datos especificos por los indices de la lista
print(f"La temperatura del primer dia es: {temperaturas[0]}")
print(f"La temperatura del ultimo dia es: {temperaturas[-1]}")
print(f"La temperatura del septimo dia es: {temperaturas[6]}")
print(f"La temperatura del penultimo dia es: {temperaturas[-2]}")

#slicing para colocar rangos de los datos
semana_1 = temperaturas[0:7]
print(f" el rango de los dias 1 a 7 es: {semana_1}")
semana_2 = temperaturas[7:15]
print(f" el rango de los dias 8 a 14 es: {semana_2}")

#dias pares de la temperatura
print(f"las temperaturas pares de la quincena son: {temperaturas[0:14:2]} ") # el tercer digito es para que se vaya saltando de 2 en 2

#orden invertido
print(f"el orden invertido de las temperaturas son : {temperaturas[::-1]}")


promedio_Semana_1 = sum(semana_1) / len(semana_1)
print(f"el promedio de la semana 1 es: {promedio_Semana_1}")
promedio_Semana_2 = sum(semana_2) / len(semana_2)
print(f"el promedio de la semana 2 es: {promedio_Semana_2}")

#bonus
mayor_promedio = max(promedio_Semana_1, promedio_Semana_2)
print(f"el promedio mayor es: {mayor_promedio}")





