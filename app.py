from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
    <title>Botón para ejecutar código Turtle</title>
    <script>
    function ejecutarCodigo() {
        fetch('/ejecutar_codigo')
            .then(response => response.text())
            .then(data => console.log(data))
            .catch(error => console.log(error));
    }
    </script>
    </head>
    <body>
    <button onclick="ejecutarCodigo()">Ejecutar Código Turtle</button>
    </body>
    </html>
    '''

@app.route('/ejecutar_codigo')
def ejecutar_codigo():
    proceso = subprocess.Popen(['python', 'codigo_turtle.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate()
    if error:
        return f'Error al ejecutar el código: {error.decode()}'
    else:
        return 'Código Turtle ejecutado con éxito'

if __name__ == '__main__':
    app.run(debug=True)
