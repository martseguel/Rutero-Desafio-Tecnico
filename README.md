# Rutero-Desafio-Tecnico

Este proyecto es una aplicación web desarrollada en Python utilizando el módulo de Flask y las bibliotecas requests y BeautifulSoup para extraer la informacion de Rutero.

## Prerrequisitos

Python. Descarga -> [Python](https://www.python.org/downloads/).

## Instalación

1. Clonar el repositorio o descargarlo como un archivo ZIP para luego extraer.

2. Abrir una terminal y navegar hasta la carpeta donde se guardó el proyecto.

3. Instalar las dependencias requeridas ejecutando el siguiente comando:

   ```bash
   pip install flask requests beautifulsoup4

## Ejecución

1. Con las dependencias instaladas, ejecutar la app desde la terminal abierta anteriormente.
   ```bash
   python main.py

2. Abrir un navegador web y entrar a la direccion:
   ```bash
   http://127.0.0.1:5000

## Uso

La app tiene dos Rutas disponibles

1. Pagina de Blog
   ```bash
   http://127.0.0.1:5000/
2. Vista especifica de un Blog
   ```bash
   http://127.0.0.1:5000/replicablog

## Detener la aplicación

Para detener la app se presiona 'ctrl+c' en la terminal donde se esté ejecutando.

## Supuestos

La pagina de Blogs, con la grilla de los articulos, obtiene unicamente los titulos e imagenes de los articulos, el numero de la paginacion que se esta consultando, total de paginas existentes, imagenes de logo de rutero y partners.
Lo demás, en cuanto a estructura y estilos, está en la estructura del html del proyecto. La funcionalidad de la paginacion, que funciona igual que la pagina original, tambien está hecha por mi y se comporta de igual manera que la original. Mi supuesto en la programacion de esta pagina se basa en cumplir con el objetivo de replicar la pagina si se agregaran mas articulos, o si se cambiara el titulo o imagen de alguno de ellos.
Por otro lado, la pagina de un blog especifico [Blog seleccionado](https://www.ruterocamping.com/blog/donde-ir-en-fiestas-patrias-tres-lugares-imperdibles-para-planificar-tu-viaje), obtiene la mayoria de la estructura de la pagina original y la replica, tambien los estilos css están conectados a los originales. Por lo tanto cumple con el supuesto objetivo de replicar el funcionamiento si se cambiara alguna informacion o estilo. Además, las animaciones tambien funcionan.
