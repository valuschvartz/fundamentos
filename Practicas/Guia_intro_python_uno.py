#!/bin/python3
# Ejercicio 1
#Escribir funciones que permitan obtener el anterior y el siguiente de un número.
def antes (numero):
    anterior = numero - 1
    return anterior
def despues (numero):
    posterior = numero + 1
    return posterior 

# Ejercicio 2
#Escribir una función que obtenga el doble de un número.
def doble (numero):
    return numero * 2

# Ejercicio 3
# Escribir funciones que obtengan el doble del anterior y el doble del siguiente de un número.
def doble_antes (numero):
    return (numero-1)* 2
def doble_despues(numero):
    return (numero + 1)* 2

# Ejercicio 4
# Escribir una función llamada retirar_dinero, que tenga como parámetros el saldo y 
# el monto a retirar y que devuelva cuánto saldo queda luego de la extracción. 
# Si retira más dinero que lo que tiene en el saldo debe devolver 0 (no se puede usar if).
def retirar_dinero (saldo, monto):
   return max(saldo-monto, 0)

# Ejercicio 5
# Escribir una función llamada dia_de_la_semana_favorito que 
# tome como parámetro un día de la semana y devuelve True si el día es "Sábado" o False 
# si es cualquier otro (no se puede usar if).
def dia_de_la_semana_favorito(dia):
    return dia == "Sábado"

# Ejercicio 6
# Escribir una función que determine si una longitud de onda 
# de una radio está dentro o fuera del rango de recepción de una antena. 
# La longitud de onda mínima que recibe la antena es 223.0 y la máxima es 586.8 (no se puede usar if).
def rango_onda (longitud):
    return longitud >= 223.0 and longitud <= 586.8

# Ejercicio 7
# Reescribir la función del punto anterior considerando, además, que 
# la longitud de onda no puede ser 314.5 porque ya está ocupada por otra radio (no se puede usar if).
def rango_onda_dos (longitud):
    return longitud >= 223.0 and longitud <= 586.8 and longitud != 314.5

# Ejercicio 8
# Escribir una función llamada tiene_descuento que tome como parámetro una edad 
# y devuelva True en caso de que la edad sea menor o igual a 12 o mayor o igual a 60. 
# En caso contrario tiene que devolver False (no se puede usar if).
def tiene_descuento (edad):
     return edad <= 12 and edad >= 60 

# Ejercicio 9
#Escribir una función xor que tome como parámetro dos booleanos 
# y retorne el booleano correspondiente con la tabla.
def xor (a, b):
    if a == b:
        return False
    else:
        return True
    
# Ejercicio 10
# Escribir una función que reciba un nombre y un apellido 
# y devuelva un saludo de bienvenida para esa persona.
def saludo (nombre, apellido) :
    return "Bienvenido" + " " + nombre +" " + apellido

# Ejercicio 11
# Escribir una función que tome como parámetro un string y 
# que, si empieza con la letra "H", nos devuelva la longitud del string.
def empieza_h (string):
    if string.startswith("H"):
        return len(string)
    else:
        return None
    
# Ejercicio 12
# Escribir una función que reciba como parámetro un string 
# y nos diga si el string empieza con "Buenos" o "Buenas".
#Opcion 1
def inicio_opcion_uno(string):
    if string.startswith("Buenas"):
        return "El string empieza con Buenas"
    else:
        return "El string empieza con Buenos"
#Opcion 2
def inicio_opcion_dos(string):
    if string.startswith("Buenos") or string.startswith("Buenas"):
        return True
    else:
        return False

# Ejercicio 13
# Escribir una función llamada es_multiplo que reciba dos números 
# y diga si el segundo es múltiplo del primero
def es_multiplo (numero_uno, numero_dos):
    if numero_uno % numero_uno == 0:
        return "Es multiplo"
    else:
        return "No es multiplo"

# Ejercicio 14
# Escribir una función que nos diga si un número es par, impar o cero.
def paridad (numero):
    if numero== 0:
        return "Es cero"
    elif numero % 2 == 0 :
        return "Es par"
    else:
        return "Es impar"

# Ejercicio 15
# Escribir una función que tome como parámetro una frase 
# y nos diga cuántas "a" (o "A") hay en la frase, utilizando for.
def cantidad_a (string) :
    contador = 0
    for letras in string:
        if "a" == letras or "A" == letras:
            contador = contador + 1
        else :
            contador = contador
    return contador 
    
# Ejercicio 16
# Escribir una función que tome como valor una cantidad de dinero y
#  nos diga por cuántos meses podemos subsistir con ese dinero, 
# tomando en cuenta que se gastan 60000 pesos por mes.
def sobrevivir (dinero):
    meses = dinero // 6000
    return "La cantidad de meses que se pueden sobrevivir son {:n}".format(meses)

print(sobrevivir(18000))