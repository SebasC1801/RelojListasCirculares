# Reloj Analógico Circular (Listas Circulares Dobles)

Mini proyecto de Estructuras de Datos que implementa un reloj analógico usando listas doblemente enlazadas circulares para segundos, minutos y horas. Un backend mínimo en `Flask` expone la hora simulada, y una interfaz web (HTML/CSS/JS) dibuja el reloj con números, marcas, selección de zona horaria y temas visuales.

## Características

- Reloj analógico con números 1–12 y marcas detalladas de minutos/horas.
- Actualización en tiempo real cada segundo.
- Selector de zona horaria (Sistema local, Bogotá, Nueva York, Madrid, Tokio).
- Selector de temas visuales (Neón Cian, Verde, Azul, Magenta, Naranja, Morado) que cambia todo el diseño del reloj.
- Estructura de datos: `ClockStructure` basada en listas circulares dobles (`ActividadListasCircularesDobles.py`).

## Requisitos

- `Python` 3.8+
- `Flask` (única dependencia de Python)

## Instalación

- Instalar Flask:

  ```bash
  pip install flask
  ```

  Opcional (entorno virtual):

  ```bash
  python -m venv .venv
  .venv\Scripts\activate  # Windows
  pip install flask
  ```

## Ejecución

1. Ejecuta el servidor:

   ```bash
   python app.py
   ```

2. Abre en el navegador:

   - `http://127.0.0.1:5000/`

3. Detener el servidor:

   - `Ctrl + C` en la terminal.

## Estructura del proyecto

```
RelojListasCirculares/
├── ActividadListasCircularesDobles.py    # Estructura de listas y lógica del reloj
├── app.py                                # Servidor Flask + hilo que hace tick
└── templates/
    └── index.html                        # Interfaz del reloj (HTML/CSS/JS)
```

## API

- `GET /time`
  - Devuelve la hora simulada en JSON:
  
    ```json
    { "hour": 13, "minute": 45, "second": 12 }
    ```

## Notas de diseño

- Frontend sin librerías externas: todo con HTML/CSS/JS nativo.
- Backend mínimo con `Flask`; no se utilizan otras librerías de Python.
- La selección de zona horaria se realiza en el navegador mediante `Intl.DateTimeFormat`.

## Ideas de mejora

- Endpoint para sincronizar la estructura interna con la hora del sistema.
- Mostrar zona horaria y/o UTC offset en la hora digital.
- Modo XL para aumentar tamaño del reloj.

## Subir a GitHub

1. Inicializa el repositorio y realiza el primer commit:

   ```bash
   git init
   git add .
   git commit -m "Proyecto: Reloj analógico con listas circulares dobles"
   ```

2. Crea la rama principal y añade el remoto (sustituye `<URL_DEL_REPO>`):

   ```bash
   git branch -M main
   git remote add origin <URL_DEL_REPO>
   ```

3. Sube los cambios:

   ```bash
   git push -u origin main
   ```

---

Autor: (tu nombre)