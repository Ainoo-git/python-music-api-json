class Cancion:

    def __init__(self, titulo, artista, duracion, popularidad):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.popularidad = popularidad

    def es_popular(self, minimo):
        return self.popularidad >= minimo

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "artista": self.artista,
            "duracion": self.duracion,
            "popularidad": self.popularidad
        }

    @staticmethod
    def from_dict(dic):
        return Cancion(
            dic["titulo"],
            dic["artista"],
            dic["duracion"],
            dic["popularidad"]
        )
