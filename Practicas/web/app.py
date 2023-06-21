from flask import Flask, render_template, request, redirect, url_for, escape

app = Flask(__name__)

prendas = {
    100: {"name": "Remera talle m", "price": 50},
    150: {"name": "Remera talle s", "price": 40}
}

@app.get("/") #decorador, generamos el /home (pagina principal)
def home(): 
    return render_template("home.html")

@app.get("/prendas/")
def get_all_prendas():
    return render_template("prendas.html", prendas=prendas)

@app.get("/prendas/<int:id>")
def get_prenda(id):
    if id in prendas:
        prenda = prendas[id]
        return render_template('prenda.html', id=id, prenda=prenda)
    else:
        return ("No existe esa prenda", 404)