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
                