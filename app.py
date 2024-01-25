from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

