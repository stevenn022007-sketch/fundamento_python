#Se declaran las variables para que el usuario las ingrese
nota_1 = float(input("ingresa la nota 1: ")) 
nota_2 = float(input("ingresa la nota 2: "))
nota_3 = float(input("ingresa la nota 3: "))
nota_maxima = 5.0

promedio = round((nota_1 + nota_2 + nota_3) / 3 ,2)
nota_falta = nota_maxima - promedio
"""
Aca se hace una condicion para que los valores no superen la nota maxima
si si entonces le imprime "error promedio", si no entonces sigue ejecutando el codigo normal
"""
if (nota_1 > nota_maxima or nota_2 > nota_maxima or nota_3 > nota_maxima):
    print("error promedio")
else:
    if(promedio >= 3.0):
        print(f"el estudiante tiene un promedio de {promedio} paso el año")
        print(f"el estudiante le falto {nota_falta} para la nota maxima")
    
    else:
        print("el estudiante reprobo")
        print(f"el estudiante le falto {nota_falta} para la nota maxima")
        
        
        
    


    
    



