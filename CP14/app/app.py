import functools
from webbrowser import get
from flask import Flask, make_response, render_template, request, jsonify, redirect, g, url_for, session, send_file
from requests import post
import utils, os
from forms import FormInicio
from db import get_db, close_db
from mensajes import mensajes
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.debug = True
app.secret_key = 'c0v1-d1sp4p3l3s#2022' #os.urandom(24)  #'Hola mundo'

if __name__ =='__main__':  
    app.run(debug = True)

def login_required(view):
    @functools.wraps(view)
    def warpped_view(**kwargs):
        if 'user_id' not in session:#'user' not in g: #.user is None:
            return redirect(url_for("login"))
        return view(**kwargs)
    return warpped_view

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
                    session.clear()
                    session['user_id'] = userDB[0]
                    resp = make_response(redirect(url_for('message')))
                    resp.set_cookie('username', user)
                   
                    return resp
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

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/message')
@login_required
def message():
    
    #return jsonify({'mensajes' : mensajes})
    return render_template('message.html', data=mensajes)

@app.route('/downloadpdf', methods=('GET', 'POST'))
@login_required
def downloadpdf():
    return send_file("resources/CP_SESION01_ENUNCIADO.pdf", as_attachment=True)