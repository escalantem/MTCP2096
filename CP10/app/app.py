from flask import Flask, render_template

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

@app.route('/registro')
def registro():
    return render_template('formulario.html')

@app.route('/OtraPagina')
def OtraPagina():
    return 'OtraPagina'
    

    