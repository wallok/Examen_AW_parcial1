from app.forms import ComisionForms
from app import app
from flask import render_template

def Calculo(monto):
    if monto>1000000:
        comision=monto-monto*0.0295
    if monto>500000:
        comision=monto-monto*0.0315
    if monto>250000:
        comision=monto-monto*0.0345
    if monto>50000:
        comision=monto-monto*0.0365
    else:
        comision=monto-5
    return comision

@app.route("/", methods=["GET","POST"] )
@app.route("/index", methods=["GET","POST"])
def index():
    form = ComisionForms()
    if form.validate_on_submit():
        monto= float(form.comision.data)
        nuevomonto = Calculo(monto)
        return render_template("resultado.html",nuevomonto=nuevomonto)
    return render_template("index.html",form=form)