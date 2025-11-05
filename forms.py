from wtforms import Form, FloatField, validators, EmailField
from wtforms import StringField, SubmitField, IntegerField, DecimalField, SelectField, RadioField, TextAreaField, PasswordField, BooleanField, DateField, DateTimeField, TimeField, FileField, FieldList, FormField
class userForm(Form):
    matricula = IntegerField('Matrícula', 
        [validators.DataRequired(message="La matrícula es obligatoria.")])
    nombre = StringField('Nombre', 
        [validators.Length(min=4, max=25), validators.DataRequired(message="El nombre es obligatorio.")])
    apellido = StringField('Apellido', 
        [validators.Length(min=6, max=35), validators.DataRequired(message="El apellido es obligatorio.")])
    correo = EmailField('Correo', 
        [validators.Email(), validators.DataRequired(message="El correo es obligatorio.")])
    submit = SubmitField('Submit')