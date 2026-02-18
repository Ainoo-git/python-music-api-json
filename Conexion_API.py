import requests

def descargar_canciones(artista):
    url = f"https://api.deezer.com/search?q={artista}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    lista_canciones = []

    for item in datos["data"]:
        cancion = Cancion(
            item["title"],
            item["artist"]["name"],
            item["duration"],
            item["rank"]
        )
        lista_canciones.append(cancion)

    return lista_canciones
