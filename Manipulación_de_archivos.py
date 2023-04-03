
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

#  **Ejercicio 5**
# Escribí un programa que lea un archivo, 
# reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

#  **Ejercicio 6**
# Realizá un programa que lea un archivo, 
# elimine todos los saltos de línea y lo guarde en otro archivo.

#  **Ejercicio 7**
# Escribí un porgrama que lea un archivo e identifique 
# la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

#  **Ejercicio 8**
# Escribí un programa que abra dos documentos y guarde 
# el contenido de ambos en un otro documento ya existente.

#  **Ejercicio 9**
# Realizá un programa que lea un archivo y obtenga 
# la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces 
# que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

#  **Ejercicio 10**
# # Escribí un programa que lea todos los archivos .txt de 
# una carpeta dada (**Carpeta1**) y los añada a un archivo dentro de 
# la carpeta _Resultado_, que a su vez se tiene que encontrar dentro de **Carpeta1**.