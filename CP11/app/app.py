from webbrowser import get
from flask import Flask, render_template, request, jsonify
import utils, os
from forms import FormInicio
from info import lista
from mensajes import mensajes

app = Flask(__name__)
app.debug = True
app.secret_key = 'c0v1-d1sp4p3l3s#2022' #os.urandom(24)  #'Hola mundo'

if __name__ =='__main__':  
    app.run(debug = True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=('GET','POST'))
def login():
    
    if(request.method =="POST"):
        formulario = FormInicio(request.form)
        
        if(formulario.validate()):
            user = request.form['usuario']
            password = request.form['contraseña']

            if (user == 'Prueba' and password =='Prueba1234'):
                return jsonify({'mensajes': mensajes})

            return 'sin acceso'
        else:
            return 'csrf error'


    formulario = FormInicio()
    return render_template('iniciar_sesion.html', form=formulario)


@app.route('/registro', methods=('GET','POST'))
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


@app.route('/api')
def api():
    #return jsonify({'message': 'hola mundo API', 'otra llave': 'algo'})
    b = lista[0]
    print(b)
    return b

@app.route('/productos')
def productos():

    return jsonify({'articulos': lista,
'menssage': 'listado de articulos'})

@app.route('/crearProducto', methods=('POST',))
def crearProducto():
    data = request.json
    print(data)
    lista.append(data)
    n = len(lista)
    return jsonify({'cantidad articulos': n})
