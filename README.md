# `README.md`

## Descripción del Proyecto

Este proyecto es un raspador web desarrollado con Scrapy, un marco de raspado y rastreo web de código abierto en Python. El objetivo principal de este proyecto es raspar la página web de Computrabajo y obtener ofertas de trabajo filtradas.

## Características

- Rastrea y raspa la página web de Computrabajo.
- Filtra y obtiene ofertas de trabajo específicas.
- Exporta los datos raspados a un archivo CSV.

## Requisitos

- Python 3.6 o superior.
- Scrapy

## Instalación

1. Clonar el repositorio.
2. Navegar hasta el directorio del proyecto.
3. Instalar las dependencias con el comando `pip install -r requirements.txt`.

## Uso

Para iniciar el raspado, ejecute el siguiente comando en la terminal:

```bash
scrapy crawl computrabajo_spider -o salida.csv
```

Los datos raspados se guardarán en un archivo CSV en el directorio del proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes, por favor abra un problema primero para discutir lo que le gustaría cambiar.

