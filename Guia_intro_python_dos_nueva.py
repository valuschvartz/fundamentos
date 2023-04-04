# # **Práctica de introducción a Python - Parte 2**


# ##### **Ejercicio 1**
# Definir un procedimiento que tome como parámetro una lista, 
# verifique si tiene el elemento "control" y le agregue el string "revisado" 
# y le quite el elemento "control".
def tiene_control (lista):
    if "control" in lista:
        ubicacion_control = lista.index("control")
        lista[ubicacion_control] = "revisado"
        lista.remove("control")
# ##### **Ejercicio 2**
# Definir un procedimiento que tome una lista como parámetro 
# y elimine el primer elemento de la lista. Hacer las verificaciones que sean necesarias.
def eliminar_primer_elemento (lista):
    if len(lista) > 0:
        del lista[0]
# ##### **Ejercicio 3**
# Definir una función que dada una lista y un elemento devuelva 
# la posición de este elemento en la lista.
def posicion (lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
# ##### **Ejercicio 4**
# Definir un procedimiento que tome como parámetros dos listas 
# y un elemento, en la que se debe eliminar el elemento de una lista y 
# agregarlo a la otra. Realizar dos versiones del ejercicio, usando un método 
# distinto para eliminar el elemento en cada versión. 
# ¿Qué problema/s tiene este procedimiento?
def dos_listas (lista, lista_uno, elemento):
    for elemento in lista:
        lista_uno.append(elemento)
        lista.remove(elemento)

# def dos_listas_otra_forma (lista, lista_uno, elemento):
#     if elemento in lista:
#         indice = lista.index (elemento)
#         lista_uno.append(elemento)
#         lista.pop(indice)
    
# ##### **Ejercicio 5**
# Escribir una función que tome como parámetro una lista de 
# enteros y devuelva una lista con valores booleanos que indique si cada 
# elemento es par o impar. Por ejemplo, para la lista `[2, 45, 108, 12, 7]`, l
# a función debería retornar `[True, False, True, True, False]`. 
# Utilizar la función realizada en la práctica anterior.
def paridad (lista_enteros):
    lista_bool = []
    for elemento in lista_enteros:
        if elemento % 2 == 0:
            lista_bool.append(True)
        else:
            lista_bool.append(False)
    return lista_bool
        

# ##### **Ejercicio 6**
# Escribir una función que lea un string y 
# devuelva un diccionario con la cantidad de apariciones de cada 
# carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, 
# por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter 
# "a" también tiene 1).

# ##### **Ejercicio 7**
# Modificá la función anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

# ##### **Ejercicio 8**
# Definir una función que dada una palabra, nos diga si el palíndromo o no.
def es_palindromo (string):
    vr = True
    i = 0
    l = len (string) - 1
    while i<len(string):
        vr = vr and string[i] == string[l] 
        i = i + 1
        l = l - 1
    return vr
# ##### **Ejercicio 9**
# Definir una función llamada `productoria` que toma como parámetro una 
# lista de números y los multiplica a todos.
def productoria(lista):
    resultado = 1
    for elemento in lista:
        resultado *= elemento
    return resultado

# ##### **Ejercicio 10**

# Creá un programa para gestionar datos de los socios de un club, el cual permita:

# * Cargar la información de los socios en un diccionario, al cual poder acceder por número de socio. Los datos que se deben almacenar son: _número_, _nombre y apellido_, _fecha de ingreso (ddmmaaaa)_, _cuota al dia (s/n)_. El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

#   **Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día**
  
#   **Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día**
  
#   **Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día**

# * Informar la cantidad de socios que tiene el club.

# * Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

# * Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

# * Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

# * Imprimir el listado de socios completos.

# Definir las funciones y/o procedimientos que creas necesarios.