from flask import Flask, render_template, request
import utils

app = Flask(__name__)
#app.config['DEBUG'] = True
app.debug = True

if __name__ =='__main__':  
    app.run(debug = True)

info= {'titulo': 'index',
    'mensaje': 'Hola mundo jinja2'
}

@app.route('/')
def index():
    return render_template('index.html', datos=info)

@app.route('/registro', methods=('GET', 'POST'))
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
   
@app.route('/OtraPagina')
def OtraPagina():
    return 'OtraPagina'
    

    