from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

prendas = [
    {"id": 1,"tipo": "pantalon","talle": 35},
    {"id": 2,"tipo": "pantalon","talle": 36},
    {"id": 3,"tipo": "pantalon","talle": 37},
    {"id": 4,"tipo": "pantalon","talle": 38},
    {"id": 18,"tipo": "saco","talle": "M"},
    {"id": 19,"tipo": "saco","talle": "L"},
    {"id": 20,"tipo": "saco","talle": "XL"}]

#Primer endpoint de la app:
@app.get("/") #decorador, generamos el /home (pagina principal)
def home(): 
    return render_template("home.html") #renderiza ese html y lo va a buscar a la carpeta template
#<p> etiqueta de html que se usa para poner texto en una pág web

@app.get("/prendas/")
def get_all_prendas():
    return render_template("prendas.html", prendas=prendas)

@app.get("/prendas/<id>")
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"

#como dominio vamos a usar un puerto/ip
#Para ver el front hacemos ctrl + click en el link (todo esto en la terminal)



"""
Tarea:
Armar la ruta /prendas que muestre todos los ítems de prendas
prendas = [{"id":1,"tipo":"pantalon","talle":42},{"id":2,"tipo":"pantalon","talle":42}"etc"]
"""
