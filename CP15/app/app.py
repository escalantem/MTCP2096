from webbrowser import get
from flask import Flask, render_template, request, jsonify, redirect
import utils, os
from forms import FormInicio
from db import get_db, close_db
from mensajes import mensajes
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.debug = True
app.secret_key = 'c0v1-d1sp4p3l3s#2022' #os.urandom(24)  #'Hola mundo'

if __name__ =='__main__':  
    #app.run(debug = True)
    app.run(host='127.0.0.1', port=443, ssl_context=('micertificado.pem', 'llaveprivada.pem'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=('GET','POST'))
def login():
    
    error = None
    db = get_db()

    if(request.method =="POST"):
        formulario = FormInicio(request.form)
        
        if(formulario.validate()):
            user = request.form['usuario']
            password = request.form['contraseña']



            userDB = db.execute('select * FROM usuario where usuario = ? ',
            (user,)
            ).fetchone()
            
            close_db()

            if userDB is not None:#(user == 'Prueba' and password =='Prueba1234'):
                
                stored_password = userDB[4]
                swClaveCorrecta = check_password_hash(stored_password, password)
                if(swClaveCorrecta):
                    return redirect('message')
                else:
                    return 'clave incorrecta.'

            
            
            return 'sin acceso, usuario no existe.'
        else:
           
            return 'csrf error'


    formulario = FormInicio()
    return render_template('iniciar_sesion.html', form=formulario)


@app.route('/registro', methods=('GET','POST'))
def registro():
    
    if request.method == 'POST':
        name = request.form['userName']
        user = request.form['user']
        password = request.form['password']
        email = request.form['userMail']
        error =[]

       
        generate_password_hash(password)

        db = get_db()
        
        if not utils.isUsernameValid(user):
            error.append('El usuario debe ser alfanumerico, o incluir . , - _')

        if not utils.isPasswordValid(password):
            print('La clave debe contener al menos una minuscula, una mayuscula y longitud de 8 caracteres')
            #error.append('La clave debe contener al menos una minuscula, una mayuscula y longitud de 8 caracteres')
            
        if not utils.isEmailValid(email):
            error.append('Correo no valido.')
        
        if len(error) == 0:
             db.execute('insert into usuario (nombre, usuario, correo, contraseña) values(?,?,?,?)',
                (name, user,email, generate_password_hash(password)))

             db.commit()

             close_db()

        
        return render_template('formulario.html', errorMessages=error)
    

    return render_template('formulario.html')

@app.route('/message')
def message():
    return jsonify({'mensajes' : mensajes})
