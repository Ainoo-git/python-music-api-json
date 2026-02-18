# Programa de música

Aplicación desarrollada en **Python** que consume una API REST pública para obtener datos musicales en formato JSON, procesarlos mediante Programación Orientada a Objetos y almacenarlos en ficheros JSON locales.

---

La aplicación:

- Se conecta a una API REST pública.
- Obtiene datos en formato JSON.
- Convierte esos datos en objetos.
- Gestiona la información mediante listas y funciones.
- Guarda y recupera datos desde ficheros JSON.
- Incluye interacción mediante menú en consola.

---

#### API utilizada

Se utiliza la API pública de Deezer:

https://api.deezer.com/search?q=artista

Características:

- No requiere autenticación.
- Devuelve datos en formato JSON.
- Permite búsquedas dinámicas por artista.

---

####  Estructura del proyecto

PYTHON-MUSIC-API-JSON/
│
├── cancion.py
├── conexion_API.py
├── Funciones.py
├── Guardar_json.py
├── Leer_json.py
└── Main.py

---

#### Programación Orientada a Objetos

Clase principal:

class Cancion

Cada objeto representa una canción con:

- titulo
- artista
- duracion
- popularidad

---

#### Manejo de JSON

El programa:

- Obtiene datos en formato JSON desde la API.
- Convierte el JSON en estructuras de Python.
- Crea objetos a partir de esos datos.
- Guarda la información en un fichero local (Canciones.json).
- Permite recuperar los datos desde el fichero.

Funciones utilizadas:

- json.dump()
- json.load()

Incluye manejo de excepciones:

- FileNotFoundError
- JSONDecodeError

---

#### Uso de estructuras de datos

Se utilizan:

- Listas de objetos
- Comprensiones de listas
- sorted() con lambda
- sum(), max(), min()

---

#### Cómo ejecutar el proyecto

1. Instalar dependencias:

pip install requests

2. Ejecutar el programa:

python main.py

---

#### Funcionalidades implementadas

- Descargar canciones desde API
- Mostrar canciones
- Obtener Top N populares
- Calcular estadísticas
- Guardar datos en JSON
- Cargar datos desde JSON
- Menú interactivo por consola

---

