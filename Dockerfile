# Usa una imagen base de Python
FROM python:3.8

# Configura el directorio de trabajo
WORKDIR /app

# Primero copia solo los requerimientos para cachear la instalación de las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Ahora copia el resto del código fuente
COPY . /app

# Instala dirb
RUN apt-get update && apt-get install -y dirb

# Expone el puerto en el que Flask se ejecutará
EXPOSE 5000

# Comando para iniciar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
