#!/bin/python3

# # Ejercicio 1
# # Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.
string = input("Ingresa una cadena: ")
if string[0].isupper():
    print("La primer letra es mayúscula.")
else:
    print("La primer letra es minúscula.")

# # Ejercicio 2
# # Escribí un programa que pida un número y diga si es positivo, negativo o 0 
# # y además informe si es par o impar (el 0 es un número par).
numero =int(input("Ingrese un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

if numero % 2 == 0 or numero == 0:
    print("El numero es par")
else:
    print("El numero es impar")


# # Ejercicio 3
# # # Escribí un programa que dado un número del 1 al 6, ingresado por teclado, 
# # muestre cuál es el número que está en la cara opuesta de un dado. 
# # Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.

numero =int(input("Ingrese un numero del 1 al 6: "))
if numero < 1 and numero > 6:
    print("Numero incorrecto")
    numero =int(input("Ingrese un numero del 1 al 6: "))
opuesto = 7 - numero
print(opuesto)

# # Ejercicio 4
# #Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, 
# # esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, 
# # en su caso, el rechazo de la entrega.
ubicacion = str(input("Ingrese la zona a la que va dirigido: "))
peso = int(input("Ingrese el peso del producto: "))
if peso > 5:
    print("No se puede enviar el producto")
else:
    None
    
if ubicacion == "América del Sur":
    precio = peso * 10.000
    print("El precio de su envio va a ser", precio)
elif ubicacion =="América Central":
    precio = peso * 15.000
    print("El precio de su envio va a ser", precio)
elif ubicacion =="América del Norte	":
    precio = peso * 18.000
    print("El precio de su envio va a ser", precio)
elif ubicacion =="Europa":
    precio = peso * 24.000
    print("El precio de su envio va a ser", precio)
elif ubicacion =="Asia":
    precio = peso * 30.000
    print("El precio de su envio va a ser", precio)
# # Ejercicio 5
# # Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. 
# # Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.
num_dia = int(input("Ingrese un número del 1 al 7: "))
if num_dia == 1:
    print("Lunes")
elif num_dia == 2:
    print("Martes")
elif num_dia == 3:
    print("Miércoles")
elif num_dia == 4:
    print("Jueves")
elif num_dia == 5:
    print("Viernes")
elif num_dia == 6:
    print("Sábado")
elif num_dia == 7:
    print("Domingo")
else:
    print("El número ingresado es incorrecto. Por favor ingrese un número del 1 al 7.")

# # Listas
# # Ejercicio 6
# # Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# # Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
lista = []
lista_dos = []
for i in range(5):
    cadena = input("Ingrese una cadena de caracteres: ")
    lista.append(cadena)
lista_dos.append(lista[::-1])
print(lista_dos)
    

# Ejercicio 7
# Creá un programa que declare una lista y la vaya llenando de números leídos 
# por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.
lista = []
numero = 0
while numero >= 0:
    numero = int(input("Ingrese un número: "))
    if numero >= 0:
        lista.append(numero)
    else:
        print("Los números ingresados son:", lista)

# Ejercicio 8
# Realizá un programa que declare tres listas lista1, lista2 y lista3, 
# donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado 
# y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 
# (es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)
lista_uno = []
lista_dos = []
lista_tres = []
for i in range(5):
    numero = int(input("Ingrese un numero: "))
    lista_uno.append(numero)
for i in range(5):
    numero = int(input("Ingrese un numero: "))
    lista_dos.append(numero)
for i in range(5):
    lista_tres.append(lista_uno[i] + lista_dos[i])
print(lista_uno)
print(lista_dos)
print(lista_tres)

    
# Ejercicio 9
# Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. 
# Se debe introducir el nombre y la edad de cada alumno por teclado. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*).
# Al finalizar se deben mostrar los siguientes datos:

# La edad máxima de todos los alumnos.
# Los alumnos que tengan la edad máxima
nombres =[]
edades = []
nombre = str(input("Ingresa tu nombre: "))
while nombre != "*":
    nombres.append(nombre)
    edad = int(input("Ingresa tu edad: "))
    edades.append(edad)
    nombre = str(input("Ingresa tu nombre: "))
print(max())
# Diccionarios
# Ejercicio 10
# Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones 
# de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas,
# por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
def contar_caracteres(string):
    contador = {}
    for caracter in string:
        if caracter not in contador:
            contador[caracter] = 1
        else:
            contador[caracter] += 1
    return contador


# Ejercicio 11
# Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.
# Ejercicio 12
# Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
# Cada alumno puede tener distinta cantidad de notas. 
# Guardá la información en un diccionario cuya claves serán los nombres de los alumnos 
# y los valores serán listas con las notas de cada alumno. El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.
def agregar_alumnos():
    
    alumnos = {}
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(cantidad_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print("Error: El alumno ya existe")
            continue
        notas = []
        nota = float(input("Ingrese la nota del alumno (-1 para terminar): "))
        while nota >= 0:
            notas.append(nota)
            nota = float(input("Ingrese la nota del alumno (-1 para terminar): "))

        alumnos[nombre] = notas
    print("Notas medias:")
    for nombre, notas in alumnos.items():
        nota_media = sum(notas) / len(notas)
        print(nombre + ": " + str(nota_media))

    return alumnos

# Funciones
# Ejercicio 13
# Creá un programa que pida dos número enteros al usuario 
# y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.
def es_multiplo (num1, num2):
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num1 % num2 == 0:
        print(num1, "es múltiplo de", num2)
    else:
        print(num1, "no es múltiplo de", num2)

# Ejercicio 14
# Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y 
# mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.


# Ejercicio 15
# Creá un programa para gestionar datos de los socios de un club, el cual permita:

# Cargar la información de los socios en un diccionario para acceder por número de socio. 
# Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), 
# cuota al dia (s/n) (el programa tiene que dejar de cargar cuando se ingrese el número 0). 
# El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

# Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día

# Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día

# Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

# Informar la cantidad de socios que tiene el club.

# Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

# Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

# Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

# Imprimir el listado de socios completos.

# Definir las funciones que creas necesarias.

def socios_fundadores ():
    socios = {
        1: {'nombre': 'Florencia', 'apellido': 'Ocampo', 'fecha_ingreso': '14092001', 'cuota_al_dia': True},
        2: {'nombre': 'David', 'apellido': 'Estévez', 'fecha_ingreso': '14092001', 'cuota_al_dia': True},
        3: {'nombre': 'Sofía', 'apellido': 'Cáceres', 'fecha_ingreso': '14092001', 'cuota_al_dia': True}
    }
    return socios

def socios_nuevos (socios):
    numero_socio = int(input("Ingrese su numero de socio"))
    nombre = int(input("Ingrese su nombre"))
    apellido = int(input("Ingrese su apellido"))
    fecha_ingreso = int(input("Ingrese su fecha de ingreso"))
    cuota_al_dia = input("La cuota está al día? (s/n): ").lower() == 's'
    socios[numero_socio] = {'nombre': nombre, 'apellido': apellido, 'fecha_ingreso': fecha_ingreso, 'cuota_al_dia': cuota_al_dia}
    print("Socio cargado con éxito.")

def informar_cantidad_socios(socios):
    cantidad = len(socios)
    print(f"El club tiene {cantidad} socios.")
    
def registrar_pago_cuotas(socios):
    num_socio = int(input("Ingrese el número de socio: "))
    socio = socios.get(num_socio)
    if socio:
        socio['cuota_al_dia'] = True
        print("Se han registrado el pago de todas las cuotas del socio.")
    else:
        print("El número de socio ingresado no existe.")
        
def modificar_fecha_ingreso(socios):
    for num_socio, socio in socios.items():
        if socio['fecha_ingreso'] == '21102017':
            socio['fecha_ingreso'] = '22102017'
    print("Se han modificado las fechas de ingreso correctamente.")
    
def dar_de_baja_socio(socios):
    nombre = input("Ingrese el nombre del socio: ")
    apellido = input("Ingrese el apellido del socio: ")
    for num_socio, socio in socios.items():
        if socio['nombre'] == nombre and socio['apellido'] == apellido:
            del socios[num_socio]
            print("Socio dado de baja con éxito.")
            return
    print("El socio ingresado no existe.")

def imprimir_listado_socios(socios):
    print("Listado de socios:")
    for num_socio, socio in socios.items():
        print(f"Socio número {num_socio}: {socio['nombre']} {socio['apellido']}, ingresó el {socio['fecha_ingreso']}, cuota al día: {socio['cuota_al_dia']}")

    
socios = socios_fundadores ()
while True:
    