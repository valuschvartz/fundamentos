#clase 15/5
import requests

respuesta = requests.get("https://api.github.com/users/octocut/orgs")
datos= respuesta.json()
print(len(datos))

# lista de nombres de las organizaciones que esta involucrado

print(respuesta)
print(respuesta.headers)
print(respuesta.status_code)