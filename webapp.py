from flask import Flask, render_template, redirect, url_for
from flask import jsonify
from flask import request
from forms import SearchForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('nota', nombre=form.username.data))
    return render_template('busqueda.html', form=form)

@app.route('/nota/<nombre>')
def nota(nombre):
    notas = open('notas.txt', 'r')
    nota_estudiante = []

    for line in notas:
        nota_personal = line.split(',')
        if nombre == nota_personal[0]:
            nota_estudiante.append({
                'estudiante' : nota_personal[0],
                'nota' : nota_personal[1]
            })
            break
        
    if not nota_estudiante:
        nota_estudiante.append({
                'estudiante' : 'El estudiante no se ha encontrado hermano, o no lo inscribieron o escribio mal viejo',
                'nota' : '0'
        })
    
    return render_template('notas.html', notas=nota_estudiante)

"""
@app.route('/', methods=['POST'])
def reclamar_por_nota():
    nombre = request.args['nombre']
    mensaje = request.json['mensaje']
    
    return 
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
