from flask import Flask, render_template, request
import utils, os
from forms import FormInicio



app = Flask(__name__)
#app.config['DEBUG'] = True
app.debug = True
app.secret_key = 'c0v1-d1sp4p3l3s#2022' #os.urandom(24)  #'Hola mundo'

if __name__ =='__main__':  
    app.run(debug = True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    formulario = FormInicio()
    return render_template('iniciar_sesion.html', form=formulario)


@app.route('/registro')
def registro():
    
    if request.method == 'POST':
        userName = request.form['user']
        password = request.form['password']
        email = request.form['userMail']
        error =[]

        if not utils.isUsernameValid(userName):
            error.append('El usuario debe ser alfanumerico, o incluir . , - _')

        if not utils.isPasswordValid(password):
            error.append('La clave debe contener al menos una minuscula, una mayuscula y longitud de 8 caracteres')
        
        if not utils.isEmailValid(email):
            error.append('Correo no valido.')
        
        
        
        return render_template('formulario.html', errorMessages=error)
    

    return render_template('formulario.html')



    

    