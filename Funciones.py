def mostrar_canciones(lista):

    if not lista:
        print("No hay canciones cargadas.")
        return

    for c in lista:
        print(c)


def top_populares(lista, n):

    ordenadas = sorted(lista, key=lambda x: x.popularidad, reverse=True)
    return ordenadas[:n]


def estadisticas(lista):

    if not lista:
        print("No hay datos.")
        return

    popularidades = [c.popularidad for c in lista]

    print("Popularidad media:", sum(popularidades) / len(popularidades))
    print("Popularidad máxima:", max(popularidades))
    print("Popularidad mínima:", min(popularidades))
