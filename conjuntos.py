#creacion de conjuntos
conjunto = set()
lenguajes = {"python","java","c++","python"}
print(lenguajes)

#metodos de modificacion
frutas = {"mango","guayaba","mora"}
frutas.add("maracuya")
frutas.add("mango")
frutas.remove("mora")
frutas.discard("papaya") #elimina; no lanza error si no existe
elem = frutas.pop()
print(frutas)

#verificar pertenencia
print("Python" in lenguajes)
print("cobol" in lenguajes)

python_devs = {"Ana","Luis","Marta","Carlos","Sofia"}
java_devs = {"Ana2","Luis","felipe","Carlos","Sofia3"}

todos = python_devs | java_devs
print(todos)

#interseccion
ambos = python_devs & java_devs
print(ambos)

#diferencia
solo_python = python_devs - java_devs
print(solo_python)

solo_java = java_devs - python_devs
print(solo_java)

#diferencia simetrica 
exclusivos = python_devs ^ java_devs
print(exclusivos)