from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "message, Hello, World!"


@app.route('/index')
def index():
    titulo = "IEVN-1003"
    listado = ['Operacion1', 'Operacion2', 'Operacion3', 'Operacion4']
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/operas', methods=['GET', 'POST'])
def operas():
    if request.method == 'POST':
        x1 = request.form.get('n1', type=float)
        x2 = request.form.get('n2', type=float)
        resultado = x1 + x2
    return render_template('operas.html', resultado=resultado)

@app.route('/distancia')
def distancia():
    titulo = "Calculo de Distancia"
    listado = []
    return render_template('distancia.html', titulo=titulo, listado=listado)


@app.route('/about')
def about():
    return "<h1>This no se que mas </h1>"

@app.route('/user/<string:user>')
def user(user):
    return "Hola " + user

@app.route('/numero/<int:num>')
def numero(num):  # ← corregido aquí
    return f"El número es {num}"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} Nombre: {}".format(id, username)

@app.route('/suma/<float:num1>/<float:num2>')
def func(num1, num2):
    return f"La suma de {num1} y {num2} es {num1 + num2}"

@app.route('/prueba')
def prueba():
    return '''
    <h1>Prueba de HTML</h1>
    <p>Esto es un párrafo en la prueba.</p>
    <ul>
        <li>Elemento de lista 1</li>
        <li>Elemento de lista 2</li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)