from flask import Flask

app = Flask(__name__)

#Primer endpoint de la app:
@app.get("/") #decorador, generamos el /home
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>" #<p> etiqueta de html que se usa para poner texto en una pág web

#como dominio vamos a usar un puerto/ip
#Para ver el front hacemos ctrl + click en el link (todo esto en la terminal)

"""
Tarea:
Armar la ruta /prendas que muestre todos los ítems de prendas
prendas = [{"id":1,"tipo":"pantalon","talle":42},{"id":2,"tipo":"pantalon","talle":42}"etc"]
"""

