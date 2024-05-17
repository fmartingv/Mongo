# Mongo

app.py:
Este script define una aplicación web simple utilizando Flask. Permite a los usuarios enviar una URL a través de un formulario web, que luego se procesa para iniciar un escaneo. La URL se pasa a una función de escaneo y se inicia en un hilo separado para no bloquear la aplicación web.

common.txt:
Archivo de texto que contiene una lista de términos o rutas comunes posiblemente utilizados en operaciones de escaneo o validación.

data.py:
Este script maneja operaciones relacionadas con los datos en MongoDB. Conecta a la base de datos MongoDB, inserta datos de ejemplo y realiza una consulta básica.

docker-compose.yml:
Archivo de configuración para Docker Compose que define los servicios necesarios para ejecutar MongoDB y la aplicación Flask en un entorno Docker.

Dockerfile:
Archivo Docker que define los pasos para construir una imagen de Docker con las dependencias necesarias para el proyecto. Instala Python, Flask y pymongo, y copia el código al contenedor.

prueba.py:
Script de Python utilizado para realizar pruebas. Este script ejecuta una función de prueba que simplemente imprime un mensaje.

requirements.txt:
Archivo que lista todas las dependencias de Python necesarias para el proyecto.

resultados.py:
Script de Python que maneja la lógica de los resultados obtenidos de las operaciones con los datos. Conecta a la base de datos MongoDB y consulta los resultados de los escaneos.

templates/index.html:
Plantilla HTML utilizada para la interfaz web de la aplicación. Define un formulario simple para que los usuarios ingresen una URL y la envíen para el escaneo.
