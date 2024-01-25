from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar_codigo', methods=['POST'])  # Cambiado a POST para enviar datos al servidor
def ejecutar_codigo():
    try:
        proceso = subprocess.Popen(['python', 'codigo_turtle.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate()
        if error:
            return f'Error al ejecutar el código: {error.decode()}', 500  # Devolver error 500 si hay un error
        else:
            return 'Código Turtle ejecutado con éxito'
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

