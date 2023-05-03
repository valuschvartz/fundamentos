#!/bin/python3
import os

# Obtenemos los nombres de los archivos
archivo1 = input("Introduce el nombre del primer archivo: ")
archivo2 = input("Introduce el nombre del segundo archivo: ")

# Intercambiamos los nombres de los archivos
os.rename(archivo1, "temp.txt")
os.rename(archivo2, archivo1)
os.rename("temp.txt", archivo2)

print("Los nombres de los archivos se han intercambiado correctamente.")
