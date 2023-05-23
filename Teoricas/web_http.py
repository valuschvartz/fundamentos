#clase 15/5
import requests

respuesta = requests.get("https://api.github.com/users/octocut/orgs")
datos= respuesta.json()
print(len(datos))

# lista de nombres de las organizaciones que esta involucrado
def lista_nombres_orgs(datos):
    lista_orgs = []
    for diccionario in datos:
        lista_orgs.append(diccionario['login'])
    return lista_orgs
print(lista_nombres_orgs(datos))
print(respuesta)
print(respuesta.headers)
print(respuesta.status_code)


#print(respuesta.headers) #me da ifo sobre mi pedido, me dice el límite de rate, dice tmb format=json, tmb el content-type
#print(respuesta.status_code) #https://http.cat/
#código asociada a la respuesta es el status code (cómo funcionó el pedido)
#error común: 500, internal server error


"""
1. Escribir las partes de la URL 
2. Qué respuesta obtenes al hacer un get en esa URL?
3. Cuál es el content type de esa respuesta?
4. Cuál es el status code de la respuesta?
5. Cuántas habilidades tiene ese pokemon?
1. 
https:// --> protocolo
pokeapi.co --> dominio
/api/v2/pokemon/ditto --> recurso
"""
#partes de la URL
#https:// es el protocolo
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
contenido = respuesta.json() #me da todos los contenidos asociados al recurso ditto, con los detalles de las habilidades, base de experiencia, forma, peso, etc. 
print(contenido.keys())

print(respuesta) #devuelve el status
print("El status code es: ",respuesta.status_code)
print(respuesta.headers) #devuelve datos del pedido (entre esos está en content-type)
print("El content type es:",respuesta.headers["Content-Type"]) #devuelve el content type, es un dato tipo json
#partes de la URL????
#conseguir las habilidades
print(contenido["abilities"])
print("ditto tiene:",len(contenido["abilities"]),"habilidades")


#/ability es el recurso, si lo hago asi solo me da todos los items de ese recurso (las url de cada habilidad)
#accedo a cada item haciendo /recurso/id, en el ejemplo: /ability/numero. Son parámetros
#vienen de una base de datos con los ítems (1,2,3,etc)
respuesta = requests.get('https://pokeapi.co/api/v2/ability/')
print(respuesta.json())

respuesta_item = requests.get('https://pokeapi.co/api/v2/ability/1')
print(respuesta_item.json())