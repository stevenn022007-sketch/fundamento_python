#Tuplas
tupla = ("uno","dos","tres")
tupla_Mixta = (1, "2", 5, True)
print(type(tupla))
# la dupla tiene que contar cn 2 items si no lo cuneta como otra cadena de valor
tupla3 = ("hola mundo" ,)
print(type(tupla3 ))

tupla_4 = tuple("hola")
print(tupla_4)

#TUPLAS Aprendices Adso
aprendices = ("Steven","Ronalt","Andres","Stepfanie","")
print(f"el aprediz es: {aprendices[4]}")
#los metodos que se pueden en la tuplas es el index() y el count() los demas no.
print(f"la cuenta del valor steven esta en la tupla solo : {aprendices.count("Steven")} vez")
print(f"el posicionamiento de Steven es: {aprendices.index("Steven")}")
#Slicing
print(f"rango de 1 hasta 4 {aprendices[0:3]}")
print(f"Rnago de 3 hasta 4 {aprendices[2:4]}")

#sumar tuplas
tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)
suma = (tupla_1 + tupla_2)
multiplicacion = tupla_1 * 3
print(f"la suma de las tuplas es: {suma}")

# metodo len()
longitud_tuplas = len(suma)
print(f"la longitud es: {longitud_tuplas}")

#Modified una tupla a lista
#se comvierte una dupla en una lista
lista_aprendices = list(aprendices)
print(f"el tipo de dato es {type(lista_aprendices)}")

#se tuliza append para colocar un dato a lo ultimo de la lista
lista_aprendices.append("Luis")
print(f"se agrego un dato´a lo ultimo de la lista {lista_aprendices}")

#empaquetar tuplas
programa_1 = "hola"
programa_2 = "fff"
programa_3 = "sssss"
tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas)

#Desempaquetar tuplas
tupla_desempaquetada = ("ADSO","SST","Topografia")
programa_1, *programa_2 = tupla_desempaquetada
print(tupla_desempaquetada)
# iterar con ciclo for la tupla
for programa_1 in tupla_desempaquetada:
    print(programa_1)