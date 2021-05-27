from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

class ComisionForms(FlaskForm):
    comision = DecimalField("Comision",validators=[DataRequired()])
    submit = SubmitField("Calcular")
    