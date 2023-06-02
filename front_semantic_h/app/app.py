from flask import Flask, render_template, request, redirect, jsonify
import requests, random
import json

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://rocky-reaches-44751.herokuapp.com/cursos"
    cursos = requests.get(url)
    datos_cursos = cursos.json()
    lentext = len(datos_cursos)
    random_cursos = {
        "curso1": datos_cursos[numero(lentext)],
        "curso2":  datos_cursos[numero(lentext)],
        "curso3":  datos_cursos[numero(lentext)],
        "curso4":  datos_cursos[numero(lentext)],
        "curso5":  datos_cursos[numero(lentext)],
        "curso6":  datos_cursos[numero(lentext)]
    }
    return render_template('Home.html', data = random_cursos)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/curso')
def curso():
    usuario_name = request.form.get('usuario')
    contraseña = request.form.get('contraseña')
    return render_template('curso.html')

@app.route('/crearcurso', methods=['GET','POST'])
def crearcurso():
    curso={"Nombre_curso": request.form.get('Nombre_curso'),
    "Descripcion": request.form.get('Descripción'),
    "Categoria": request.form.get('Categoria'),
    "Subtema":request.form.get('Subtema'),
    "Audiencia": request.form.get('Audiencia'),
    "Instituto":request.form.get('Instituto'),
    "Competencias": request.form.get('Competencias'),
    "Fecha_inicio": request.form.get('Fecha_inicio'),
    "Fecha_fin": request.form.get('Fecha_fin'),
    "plataforma": request.form.get('plataforma'),
    "URL_cuso": request.form.get('URL_cuso'),
    "Duración": request.form.get('Duración'),
    "semanas": request.form.get('semanas'),
    "horas": request.form.get('horas'),
    "Progreso": request.form.get('Progreso'),
    "Costo": request.form.get('Costo'),
    "nivel": request.form.get('nivel'),
    "Idioma": request.form.get('Idioma')}
    
    return 

@app.route('/recomendaciones/', methods=['GET','POST'])
def recomendaciones():
    usuario_name = request.form.get('usuario')
    contraseña = request.form.get('contraseña')
    usuarioid=usuario_name.replace('Persona','')
    usuarioid=int(usuarioid)
    valcon = "abc123" + str(usuarioid)
    if usuarioid > 50:
        return render_template('login.html')
    else:
        if contraseña == valcon:
            datos = extraccion_recomendaciones(usuario_name)
            return render_template('recomendaciones.html', data = datos)
        else:
            return render_template('login.html')
        

def extraccion_recomendaciones(usuario_name):
    url1 = "https://rocky-reaches-44751.herokuapp.com/cursoPorNivel/"+usuario_name
    cursoPorNivel = requests.get(url1)
    d_cursoPorNivel = cursoPorNivel.json()
    url2 = "https://rocky-reaches-44751.herokuapp.com/cursoPorHora/"+usuario_name
    cursoPorHora = requests.get(url2)
    d_cursoPorHora = cursoPorHora.json()
    url3 = "https://rocky-reaches-44751.herokuapp.com/cursoPorSubject/"+usuario_name
    cursoPorSubject = requests.get(url3)
    d_cursoPorSubject = cursoPorSubject.json()
    url4 = "https://rocky-reaches-44751.herokuapp.com/cursoPorProgreso/"+usuario_name
    cursoPorProgreso = requests.get(url4)
    d_cursoPorProgreso = cursoPorProgreso.json()
    url5 = "https://rocky-reaches-44751.herokuapp.com/cursoPorIdioma/"+usuario_name
    cursoPorIdioma = requests.get(url5)
    d_cursoPorIdioma = cursoPorIdioma.json()
    url6 = "https://rocky-reaches-44751.herokuapp.com/curso_persona/"+usuario_name
    cursosinscritos = requests.get(url6)
    d_cursosinscritos = cursosinscritos.json()
    datos= {"usuario": usuario_name,
            "inscritos": d_cursosinscritos,
            "cursoPorNivel": d_cursoPorNivel,
            "cursoPorHora": d_cursoPorHora,
            "cursoPorSubject": d_cursoPorSubject,
            "cursoPorProgreso": d_cursoPorProgreso,
            "cursoPorIdioma": d_cursoPorIdioma,
            }
    return datos

def numero(lentext):
    numero = random.randint(0, lentext)
    var = "Curso"+ str(numero)
    return var

if __name__ == '__main__':
    app.run(debug=True, port=5000)
