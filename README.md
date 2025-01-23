# 🕵️‍♂️ **Proyecto de Escaneo con Flask y MongoDB** 🖥️

Este proyecto implementa una **aplicación web** utilizando Flask y MongoDB para realizar escaneos de URLs. A continuación, se describe cada uno de los archivos presentes en el repositorio.

---

## 🚀 **Arquitectura del Proyecto**

### 🐍 **Archivos Principales**

1. **`app.py`** 📱  
   Este script define la aplicación web con **Flask**. Permite a los usuarios enviar una URL a través de un formulario y luego inicia un escaneo en un hilo separado para que no se bloquee la aplicación web.

2. **`common.txt`** 📄  
   Un archivo de texto que contiene una lista de **términos comunes** o rutas frecuentemente usadas en operaciones de escaneo o validación.

3. **`data.py`** 🗂️  
   Maneja la **conexión a MongoDB** y realiza operaciones como insertar datos de ejemplo y consultas básicas a la base de datos.

4. **`docker-compose.yml`** 🐳  
   Configura los servicios necesarios para ejecutar **MongoDB** y la aplicación **Flask** en un entorno de Docker, permitiendo una fácil implementación.

5. **`Dockerfile`** 🏗️  
   Define los pasos para construir una imagen Docker que incluye **Python**, **Flask**, **pymongo**, y el código fuente necesario.

6. **`prueba.py`** 🔧  
   Script para ejecutar pruebas simples, que imprime un mensaje para verificar que todo funciona correctamente.

7. **`requirements.txt`** 📋  
   Lista todas las **dependencias** necesarias para el proyecto, como **Flask**, **pymongo**, y otras bibliotecas esenciales.

8. **`resultados.py`** 🧑‍💻  
   Maneja la lógica para procesar los **resultados** de los escaneos y consulta los datos obtenidos en la base de datos **MongoDB**.

9. **`templates/index.html`** 🌐  
   Plantilla HTML para la interfaz de usuario de la aplicación web. Aquí se define el formulario para que los usuarios ingresen la URL a escanear.

---

## ⚙️ **Instrucciones para Ejecutar el Proyecto**

1. **Instala las dependencias**:
   
   `pip install -r requirements.txt`

2. **Configura Docker**:  
   Si deseas ejecutar el proyecto usando Docker, asegúrate de tener Docker y Docker Compose instalados. Luego, corre el siguiente comando para levantar los servicios:

   `docker-compose up --build`

3. **Ejecuta la aplicación**:  
   Si prefieres no usar Docker, simplemente ejecuta el archivo `app.py`:

   `python app.py`

4. **Accede a la aplicación**:  
   Abre tu navegador y visita:

   `http://127.0.0.1:5000/`

---

## 📊 **Flujo del Proyecto**

1. El usuario ingresa una URL en el formulario web.
2. La URL es procesada por **`app.py`** y se inicia un escaneo en segundo plano.
3. Los resultados se guardan en **MongoDB**.
4. Los resultados se pueden consultar a través de **`resultados.py`**.

---

## 💡 **Características**:

- 🔄 **Escaneo en segundo plano**: No bloquea la aplicación principal.
- 📚 **Base de datos MongoDB** para almacenar los resultados de los escaneos.
- 🐳 **Dockerizado** para fácil implementación y escalabilidad.
- 🧪 **Pruebas simples** para verificar el funcionamiento.

