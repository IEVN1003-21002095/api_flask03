from flask import Flask, jsonify, render_template, request, make_response

import forms
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "message, Hello, World!"


@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    mat = 0
    nom = ""
    ape = ""
    em = ""
    estudiantes = []
    tem={}
    datos = {"matricula":mat,"nombre":nom,"apellido":ape,"correo":em} 
    datos_str = request.cookies.get('estudiantes')
    alumnos_clase = forms.userForm(request.form)
    if request.method == 'POST' and alumnos_clase.validate():
        mat = alumnos_clase.matricula.data
        nom = alumnos_clase.nombre.data
        ape = alumnos_clase.apellido.data
        em = alumnos_clase.correo.data
        datos = {"matricula": mat,"nombre": nom,"apellido": ape,"correo": em }
        
    datos_str = request.cookies.get('estudiantes')
    if not datos_str:
     return "No hay datos de estudiantes en las cookies."
    tem=json.loads(datos_str)
    estudiantes=tem
    estudiantes.append(datos)
    response = make_response(render_template("Alumnos.html",form=alumnos_clase,mat=mat,nom=nom,ape=ape,em=em))
    response.set_cookie('estudiante', json.dumps(estudiantes))
    return response

@app.route('/get_cookie')
def get_cookie():
    datos_str = request.cookies.get('estudiantes')
    if not datos_str:
        return "No hay datos de estudiantes en las cookies."
    datos=json.loads(datos_str)
    return jsonify(datos)
    
@app.route('/Figuras', methods=['GET', 'POST'])
def figuras():
     area = 0
     figura = None
     base = 0
     altura = 0
     radio = 0
     figuras_clase = figurasForm.calculoAreaCirculo(request.form)
     if request.method == 'POST' and figuras_clase.validate():
         area = figuras_clase.area
         radio = figuras_clase.radio.data
         altura = 0
         base = 0
         return render_template('figuras.html', form=figuras_clase, 
                                area=area, figura=figura, radio=radio,
                                base=base, altura=altura)
     return render_template('figuras.html', form=figuras_clase,
                            area=area, figura=figura, radio=radio,
                            base=base, altura=altura)

@app.route('/index') 
def index():
    titulo = "IEVN-1003"
    listado = ['Operacion1', 'Operacion2', 'Operacion3', 'Operacion4']
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/operas', methods=['GET', 'POST'])
def operas():
    resultado = None
    if request.method == 'POST':
        x1 = request.form.get('n1', type=float)
        x2 = request.form.get('n2', type=float)
        resultado = x1 + x2
    return render_template('operas.html', resultado=resultado)

@app.route('/distancia')
def distancia():
    titulo = "Calculo de Distancia"
    return render_template('distancia.html', titulo=titulo)


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