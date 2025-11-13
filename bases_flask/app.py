from flask import  Flask,render_template, request, make_response, jsonify

import bases_flask.forms as forms
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "message, Hello, World!"

@app.route('/Pizzeria', methods=['GET', 'POST'])
def pizzeria():
    form = forms.pizzaForm(request.form)

    precios_tamano = {"Chica": 40, "Mediana": 80, "Grande": 120}
    precio_ingrediente = 10

    pedidos = json.loads(request.cookies.get('pedidos')) if request.cookies.get('pedidos') else []
    ventas_dia = json.loads(request.cookies.get('ventas')) if request.cookies.get('ventas') else []

    mensaje_total = None
    mostrar_ventas = False  

    if request.method == 'POST':
        accion = request.form.get("accion")

        if accion == "agregar":
            tam = request.form.get("tamannio")
            ingredientes = request.form.getlist("ingredientes")
            num = int(request.form.get("num_pizzas"))

            subtotal = (precios_tamano[tam] + len(ingredientes) * precio_ingrediente) * num

            pedidos.append({
                "tamannio": tam,
                "ingredientes": ingredientes,
                "num_pizzas": num,
                "subtotal": subtotal
            })

        if "quitar" in request.form and len(pedidos) > 0:
            pedidos.pop()  

        if accion == "terminar":
            total = sum(p["subtotal"] for p in pedidos)
            mensaje_total = f"El total de su pedido es: ${total}"

            venta = {
                "nombre": form.nombre.data,
                "direccion": form.direccion.data,
                "telefono": form.telefono.data,
                "total": total
            }

            encontrado = False
            for v in ventas_dia:
                if v["nombre"] == venta["nombre"] and v["telefono"] == venta["telefono"]:
                    v["total"] += total
                    encontrado = True
                    break

            if not encontrado:
                ventas_dia.append(venta)

            pedidos = []

        if accion == "ver_ventas":  
            mostrar_ventas = True

    total_dia = sum(v["total"] for v in ventas_dia)

    response = make_response(render_template(
        "Pizzeria.html",
        form=form,
        pedidos=pedidos,
        ventas_dia=ventas_dia,
        total_dia=total_dia if mostrar_ventas else None,
        mensaje_total=mensaje_total
    ))

    response.set_cookie('pedidos', json.dumps(pedidos))
    response.set_cookie('ventas', json.dumps(ventas_dia))

    return response

@app.route('/Alumnos', methods=['GET', 'POST'])
def alumnos():
    # Initialize form and default values
    alumnos_clase = forms.userForm(request.form)
    estudiantes = []

    # Retrieve existing students from cookies
    datos_str = request.cookies.get('estudiantes')
    if datos_str:
        try:
            estudiantes = json.loads(datos_str)
        except json.JSONDecodeError:
            estudiantes = []
    else:
        estudiantes = []
    if request.method == 'POST' and alumnos_clase.validate():
        datos = {
            "matricula": alumnos_clase.matricula.data,
            "nombre": alumnos_clase.nombre.data,
            "apellido": alumnos_clase.apellido.data,
            "correo": alumnos_clase.correo.data
        }
        estudiantes.append(datos)
    else:
        datos = {
            "matricula": 0,
            "nombre": "",
            "apellido": "",
            "correo": ""
        }
    response = make_response(render_template(
        "Alumnos.html",
        form=alumnos_clase,
        mat=datos["matricula"],
        nom=datos["nombre"],
        ape=datos["apellido"],
        em=datos["correo"]
    ))
    response.set_cookie('estudiantes', json.dumps(estudiantes))
    return response


@app.route('/get_cookie')
def get_cookie():
    pedidos_str = request.cookies.get('pedidos')
    if not pedidos_str:
        return "No hay datos de pedidos en las cookies."
    pedidos=json.loads(pedidos_str)
    return jsonify(pedidos)

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