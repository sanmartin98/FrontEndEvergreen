from flask import Flask, jsonify,request,render_template,request
import requests

app = Flask(__name__,template_folder='templates')

personaEncargada = ['Camilo Sanmartin','Juan Bernardo','Andres Arango','Santiago Castaneda','Daniela Villegas']

modulos = ['Suministro','Producción','Distribución','Planeación','Finanzas','Administración','Configuración','Mensajería']


@app.route("/guardarProyecto",methods=['POST'])
def guardarProyecto():
    proyectos = dict(request.values)
    proyectos['estado'] = 'En desarrollo'
    requests.post('http://34.73.204.3/proyectosAnalitica',json=proyectos)
    return(listarProyectos())


@app.route('/crearProyecto',methods=['Get'])
def crearProyecto():
    return render_template('crearProyectoAnalitica.html',modulos=modulos,personaEncargada=personaEncargada)


@app.route('/listarProyectos',methods=['Get'])
def listarProyectos():
    proyectos = requests.get('http://34.73.204.3/proyectosAnalitica').json()
    return render_template('listarProyectoAanalitica.html',proyectos=proyectos)

if __name__ == '__main__':
    app.run()