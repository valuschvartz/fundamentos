import os, glob, sys 
def ejercicio_rutas():
    os.chdir("Informes")
    txt = glob.glob("*.txt")
    cantidad_estado = []
    cantidad_lineas = []
    for archivo in txt:
        with open(archivo, "r") as file: 
            fila_completa = file.read()
            cantidad_estado.append(fila_completa.count("estado"))
            cantidad_lineas.append(fila_completa.count("\n"))
    os.mkdir("Apellido")
    with open ("Apellido/Lista.txt", "w") as salida:
        for archivo in txt:
            with open ("archivo", "r") as file:
                primer_linea = file.readlines()
                salida.write(primer_linea)
#5/04
#Guia Manipulacion Archivos
#
#Ejericio 1
def start_with(letra,archivo):
    count=0
    with open(archivo,"r") as archivo:
        for linea in archivo:
            if (linea[0] != letra.lower() or linea[0] != letra.upper()):
                count += 1
    print("El número de líneas que no empiezan con", letra, "es", count)

start_with("H","archivo1.txt")

#Ejercicio 2
def read_n_lines(n,archivo):
    with open(archivo,"r") as file:
        for i in range(n):
            print(file.readline())
read_n_lines(2,"archivo1.txt")

#Ejercicio 3
def read_n_back_lines(n, archivo):
    texto = open(archivo, "r").readlines()
    for i in range((len(texto)-n), len(texto)):
        print(texto[i])

read_n_back_lines(2,"archivo1.txt")

#Ejercicio 7
def longest_word(archivo):
    max_long = 0
    palabra = ""
    with open(archivo,"r") as f:
        word_list = f.read().split()
        for word in word_list:
            if len(word) > max_long:
                max_long = len(word)
                palabra = word
    print("La palabra más larga es", palabra, "con", max_long, "caracteres")
longest_word("archivo1.txt")

#Ejercicio 8
def join_files(file1,file2,file3):
    with open(file1,"r") as f1, open(file2, "r") as f2, open(file3,"a") as f3:
        f3.write(f1.read()+f2.read())
join_files("archivo1.txt","archivo2.txt","archivos_unidos.txt")

#Ejercicio repaso 3/5
#Definir un procedimiento que lea los archivos .txt que estan en la carpeta de marzo, y copie la primera
#lineaa de cada uno en un archivo dentro de la carpeta resultados (que debe estar dentro de new)
import os, glob

def primeras_lineas ():
    os.chdir("Marzo")
    txt = glob.glob(".txt")
    primera_linea = []
    for archivo in txt:
        with open(archivo, "r") as file: 
            fila_completa = file.readline()
            primera_linea.append(fila_completa)
    os.chdir("../../") 
    os.mkdir("Resultado")
    with open ("Resultado/Lista.txt", "a") as salida:
        for linea in primera_linea:
            salida.write(linea)
#12/04
#Guia Expresiones Regulares
#
#Ejericio 1
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. 
#Estos caracteres son a-z, A-Z y 0-9.
import re
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z]', string)) #Transformo el resultado en booleano (true o false) todo valor vacío es true
"""print(bool(4)) #Devuelve true
print(bool(None)) #Devuelve falso"""
print(caracteres_permitidos("ABCja578"))

#Ejercicio 2
#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son
# a-z, A-Z y 0-9
import re
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z]', string)) 
print(caracteres_permitidos("Hola"))

#Ejercicio 3
#Creá un programa que verifique las siguientes condiciones:

#si un string dado tiene una h seguida de ninguna o más e.

import re
#a)
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron,string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
#Lo que estpa 0 o más veces es la "e"
print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeee"))

#si un string dado tiene una h seguida de una o más e.

import re
#b)
def encontrar_patron(string):
    patron = "he+"
    if re.search(patron,string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
#Lo que estpa 0 o más veces es la "e"
print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeee"))

#si un string dado tiene una h seguida de cero o una e.
import re   
def encontrar_patron(string):
    patron = "he?"
    if re.search(patron,string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
#Lo que estpa 0 o más veces es la "e"
print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeee"))

#Después de la e puede haber cualquier cosa

#si un string dado tiene una h seguida de dos o tres e.
import re   
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron,string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
#Lo que estpa 0 o más veces es la "e"
print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeee"))
#mientras tenga entre 2 y 3 e, lo demás puede ser cualquier letra

#Ejercicio 4
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
import re   
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Patrón encontrado"
    else:
        return "Patrón no encontrado"
#cadena = input("ingresa una cadena: ")

#Ejercicio 8
#Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
def extraer_numeros(string):
    resultado = re.split("\D+", string)
    for elemento in resultado:
        print(elemento)
string = "Hoy movimos 10 cajas de lugar, en 3 edificios distintos para llevar a 12 casas"
print(extraer_numeros(string))

#Ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un
# string. (String de ejemplo: "Hoy estuvimos trabajando con re
# -regular expression- en python -con VSCode-")
import re
def entre_guiones(string):
    return re.findall(r"-(.*?)-",string) #devuelve una lista con los patrones
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(entre_guiones(string))
#Cuando usamos el signo de pregunta así, favorecemos los matches internos, no ve solo lo global
#si no pongo el signo va a devolver: -regular expression- en python -con VSCode- porque no vería los guiones en el medio
#No devuelve el "en python" porque ya usó el guión del comienzo para cerrar el anterior.

#Ejercicio 10
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
import re
def get_substr(string):
    return re.findall("[@|$](.*?)[@|&]", string)
string = "cdaf@dsfe% ad @ sd"
print(get_substr(string))

#Ejercicio 11
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra 
#P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
import re
def dos_P(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento) #Puedo poner \W o \S (espacio). Puedo usar * o +.
        if resultado is not None:
            print(resultado.group())
lista = ["Práctica Python","Práctica C++", "Práctica Fortran"]
dos_P(lista)