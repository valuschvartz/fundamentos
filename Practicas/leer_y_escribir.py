#!/bin/python3
# with open("texto_random.txt","a") as mi_archivo :
#     mi_archivo.write("Hola")

   
with open("archivo.txt", "r") as mi_archivo:
    with open("texto_random.txt", "a") as nuevo :
        nuevo.write(mi_archivo.readline(5))