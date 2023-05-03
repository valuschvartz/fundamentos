
# **Ejercicio 1**
# Realizá un programa que lea un archivo e 
# imprima cuántas líneas de ese archivo **no** empiezan con una
# determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
def empieza_con(archivo, letra):
    with open(archivo, 'r') as file: 
        fileContent = file.readlines()
    for fileline in fileContent: 
        no_empieza_con = 0 
        if not str.startswith(fileline, letra): 
            no_empieza_con += 1
        print(no_empieza_con)

#  **Ejercicio 2**
# Escribí un programa que lea un archivo e imprima las primeras n líneas.
def imprimir_n_lineas (archivo, n):
    with open(archivo, "r") as file:
        lineas = file.readlines()[:n]
        for linea in lineas:
            print(linea.rstrip())
#  **Ejercicio 3**
# Escribí un programa que lea un archivo, guarde 
# las líneas del archivo en una lista y luego imprima las n últimas.
def guardar_lineas(archivo, n):
    with open(archivo, "r") as file:
        lineas = file.readlines()[:n]
        lista = []
        for linea in lineas:
            lista.append(linea)
            print(linea.rstrip())
        

#  **Ejercicio 4**
# Hacé un programa que lea un archivo, cuente la cantidad de palabras 
# del archivo y luego imprima el resultado.
def cantidad_palabras(archivo):
    with open (archivo, "r") as file:
        contador = 0
        lineas = file.readlines()
        for linea in lineas:
            palabras = linea.split()
            contador = contador + len(palabras)
#  **Ejercicio 5**
# Escribí un programa que lea un archivo, 
# reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

def reemplazar_letra (archivo, archivo_dos, letra):
    with open (archivo, "r") as file:
        with open (archivo_dos, "w") as file_2:
            for n in file:
                n = n.replace(letra, letra+'\n')
            file_2.write(n)

#  **Ejercicio 6**
# Realizá un programa que lea un archivo, 
# elimine todos los saltos de línea y lo guarde en otro archivo.
def eliminar_saltos_de_linea(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as file_1:
        with open(archivo_salida, 'w') as file_2:
            for linea in file_1:
                linea_sin_salto = linea.rstrip('\n')
                file_2.write(linea_sin_salto)


#  **Ejercicio 7**
# Escribí un porgrama que lea un archivo e identifique 
# la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.


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


#  **Ejercicio 8**
# Escribí un programa que abra dos documentos y guarde 
# el contenido de ambos en un otro documento ya existente.

def join_files(file1,file2,file3):
    with open(file1,"r") as f1, open(file2, "r") as f2, open(file3,"a") as f3:
        f3.write(f1.read()+f2.read())
join_files("archivo1.txt","archivo2.txt","archivos_unidos.txt")


#  **Ejercicio 9**
# Realizá un programa que lea un archivo y obtenga 
# la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces 
# que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def frecuencia (archivo):
    with open (archivo, "r") as file:
        fileContent = file.readlines()
        for fileline in fileContent: 
            hola = 1 + hola
            
            


#  **Ejercicio 10**
# Escribí un programa que lea todos los archivos .txt de 
# una carpeta dada (**Carpeta1**) y los añada a un archivo dentro de 
# la carpeta _Resultado_, que a su vez se tiene que encontrar dentro de **Carpeta1**.

import glob, os
def leer_archivos (archivos):
    txt= glob.glob (".txt")
    
    with open (archivos, "a") as file:
        