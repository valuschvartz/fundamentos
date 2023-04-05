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

