def main():
    canciones = []

    while True:
        print("\n1. Descargar desde API")
        print("2. Mostrar canciones")
        print("3. Top populares")
        print("4. Guardar en JSON")
        print("5. Cargar desde JSON")
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
            guardar_json(canciones, "canciones.json")

        elif opcion == "5":
            canciones = cargar_json("canciones.json")

        elif opcion == "0":
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
