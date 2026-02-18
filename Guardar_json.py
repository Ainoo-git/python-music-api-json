import json

def guardar_json(lista, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in lista], f, indent=4, ensure_ascii=False)
