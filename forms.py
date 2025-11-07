from wtforms import Form, validators, EmailField
from wtforms import StringField, SubmitField, IntegerField,  RadioField, SelectMultipleField, validators
from wtforms.validators import DataRequired, Length, NumberRange
class alumnosForm(Form):
    matricula = IntegerField('Matrícula', 
        [validators.DataRequired(message="La matrícula es obligatoria.")])
    nombre = StringField('Nombre', 
        [validators.Length(min=4, max=25), validators.DataRequired(message="El nombre es obligatorio.")])
    apellido = StringField('Apellido', 
        [validators.Length(min=6, max=35), validators.DataRequired(message="El apellido es obligatorio.")])
    correo = EmailField('Correo', 
        [validators.Email(), validators.DataRequired(message="El correo es obligatorio.")])
    submit = SubmitField('Submit')

class pizzaForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    num_pizzas = IntegerField('Número de Pizzas', validators=[DataRequired()])
    submit = SubmitField('Submit')