#se crea las listas de producto y precio y cantidades
producto = ["Lapiceros","Cuadernos","Borradores","Colores","Reglas","libros",]
precio = ["1800","5000","1200","8000","5000","30000"]
cantidades = [1, 2, 3 ,4 , 6, 8]
# Se halla la longitud de la,llista de productos
cantidad_productos = len(producto)
#se imprime las listas 
print("inventario de productos:" 
      "\n producto:  ", producto,
      "\n cantidad: ", cantidades,
      "\n precio :", precio,
      "\n cantidade de productos:  ", cantidad_productos)
"\n"
# se imprime el tipo de las tres listas
print("inventario de productos:" 
      "\n producto:  ", type(producto),
      "\n cantidad: ", type(cantidades) ,
      "\n precio :", type(precio) ,
      "\n cantidade de productos:  ", type(cantidad_productos) )
#se imprime el tipo de del valor o de la lista.
print("inventario de productos:" 
      "\n producto:  ", type(producto[0]),
      "\n cantidad: ", type(cantidades[0]) ,
      "\n precio :", type(precio[0]) )


