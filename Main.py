from Conexion_API import descargar_canciones
from Funciones import mostrar_canciones, top_populares, estadisticas
from Guardar_json import guardar_json
from Leer_json import cargar_json

def main():

    canciones = []

    while True:

        print("\n MENÚ")
        print("1. Descargar desde API")
        print("2. Mostrar canciones")
        print("3. Top N populares")
        print("4. Estadísticas")
        print("5. Guardar en JSON")
        print("6. Cargar desde JSON")
        print("0. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            artista = input("Artista: ")
            canciones = descargar_canciones(artista)

        elif opcion == "2":
            mostrar_canciones(canciones)

        elif opcion == "3":
            n = int(input("¿Cuántas?: "))
            top = top_populares(canciones, n)
            mostrar_canciones(top)

        elif opcion == "4":
            estadisticas(canciones)

        elif opcion == "5":
            guardar_json(canciones, "canciones.json")

        elif opcion == "6":
            canciones = cargar_json("canciones.json")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
