def mostrar_canciones(lista):
    for c in lista:
        print(c.titulo, "-", c.artista)

def top_populares(lista, n):
    ordenadas = sorted(lista, key=lambda x: x.popularidad, reverse=True)
    return ordenadas[:n]
