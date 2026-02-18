import requests
from Cancion import Cancion

def descargar_canciones(artista):

    try:
        url = f"https://api.deezer.com/search?q={artista}"
        respuesta = requests.get(url)
        respuesta.raise_for_status()

        datos = respuesta.json()

        if not datos["data"]:
            print("No se encontraron resultados.")
            return []

        lista = []

        for item in datos["data"]:
            lista.append(
                Cancion(
                    item["title"],
                    item["artist"]["name"],
                    item["duration"],
                    item["rank"]
                )
            )

        print(f"Se descargaron {len(lista)} canciones.")
        return lista

    except requests.exceptions.RequestException:
        print("Error al conectar con la API.")
        return []
