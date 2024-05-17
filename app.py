from flask import Flask, request, render_template
from pymongo import MongoClient
import subprocess
import shlex
import os
from threading import Thread

app = Flask(__name__)

# Configuración de la conexión a MongoDB
client = MongoClient('mongodb://db:27017/')
db = client['webscraping']
resultados = db['resultados']

# Obtén la ruta absoluta del archivo common.txt
ruta_comun = os.path.join(os.path.dirname(__file__), 'small-list.txt')

# Definición de la función de escaneo que se ejecutará en un hilo
def scan_url(url, ruta_comun):
    comando_dirb = f"dirb {url} {ruta_comun}"
    args = shlex.split(comando_dirb)
    proceso = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate()

    if proceso.returncode == 0:
        for linea in salida.decode().split('\n'):
            if linea.strip() and "FOUND" in linea:
                resultados.insert_one({"url": url, "resultado": linea.strip()})
    else:
        print(f"Error al escanear {url}: {error.decode()}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        thread = Thread(target=scan_url, args=(url, ruta_comun))
        thread.start()
        # Informa al usuario que el escaneo ha comenzado
        return f"Escaneo iniciado para: {url}. Verifique más tarde para los resultados."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
