import json
from Cancion import Cancion

def cargar_json(nombre_archivo):

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        lista = [Cancion.from_dict(d) for d in datos]
        print("Datos cargados correctamente.")
        return lista

    except FileNotFoundError:
        print("El archivo no existe.")
        return []

    except json.JSONDecodeError:
        print("Error al leer el JSON.")
        return []
