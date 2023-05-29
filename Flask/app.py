from flask import Flask, render_template
from markupsafe import escape 

prendas = [
    {"id": 1, "tipo": "pantalon", "talle": 42},
    {"id": 2, "tipo": "pantalon", "talle": 56},
]


app = Flask(__name__)

#Primer endpoint de la app:
@app.route("/") #decorador, generamos el /home
def home():
    return render_template ("home.html")

#como dominio vamos a usar un puerto/ip
#Para ver el front hacemos ctrl + click en el link (todo esto en la terminal)

@app.route("/prendas")
def get_all_prendas ():
    return f"<p> Mostrando todas las prendas </p>"

@app.route("/prendas/<id>")
def get_prenda (id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"



"""
Tarea:
Armar la ruta /prendas que muestre todos los ítems de prendas
prendas = [{"id":1,"tipo":"pantalon","talle":42},{"id":2,"tipo":"pantalon","talle":42}"etc"]
"""
