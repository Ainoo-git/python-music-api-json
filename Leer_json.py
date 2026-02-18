def cargar_json(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        datos = json.load(f)

    return [Cancion.from_dict(d) for d in datos]
