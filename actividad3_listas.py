#se crea una lista de canciones favoritas
canciones = ["Esclava","Starboy","Call out my name","Nena maldicion","loca"]
#se agrega a lo ultimo de la lista una cancion
canciones.append("De las dos")
print(f"se agrego una nueva cancion a lo ultimo de la lista {canciones}")
#se inserta una nueva cancion en el idnice 2 de la lista
canciones.insert(2, "tu eres mi perdicion")
print(f"se agrego una nueva cancion en el indice 2 {canciones}")
#se crea una lista de bonus
bonus = ["Bonus Track 1", "Bonus Track 2"]
#se combina las listas canciones con bonus
canciones.extend(bonus)
print(f"se combina las tablas canciones y bonus {canciones} ")
#se elimina la cancion por su nombre
canciones.remove("loca")
print(f"se elimino la cancion loca de la lista de canciones : {canciones}")
# Se elimina por el indice de la lista
canciones.pop(5)
print(f"se elimino la cancion 'de las dos' de la lista de canciones : {canciones}")
#Se ordena alfabeticamente las canciones
canciones.sort()
print(f"el orden alfabeticamente es {canciones}")
#calcular cuantas canciones tiene la lista
print(f"El numero de canciones son {len(canciones)}")
#posicionamiento de la primera cancion agregada 
index_poscicion = canciones.index("tu eres mi perdicion")
print(f"La posicion de la pirmera cancion agregada es: {index_poscicion} ")
# las veces que sale 'Bonus Track 1'
count_Canciones = canciones.count("Bonus Track 1")
print(f"el numero de veces que sale Bonus Track 1 es: {count_Canciones}")


