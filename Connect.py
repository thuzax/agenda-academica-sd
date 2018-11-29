from flask import Flask, redirect, url_for, request, Response
from controller.ControllerGrupo import ControllerGrupo
from controller.ControllerUsuario import ControllerUsuario
from controller.ControllerTarefa import ControllerTarefa
import json
app = Flask(__name__)

todo = {}

@app.route('/')
def root():
    return json.dumps(todo)

@app.route('/adicionar',methods = ['POST'])
def adicionar():
    id_item = request.form["id_item"]
    try:
        todo[id_item]
        response = Response(json.dumps({"mensagem" : "Item já existente"}), status=200, mimetype='application/json')
        return response
    except KeyError:
        todo[id_item] = request.form["dados"]
        response = Response(json.dumps(todo), status=200, mimetype='application/json')
        ControllerGrupo().adicionarGrupo()
        ControllerUsuario().adicionarUsuario()
        ControllerTarefa().adicionarTarefa()
        print(response)
        return response
    
@app.route('/buscar', methods = ['GET'])
def buscar():
    id_item = request.form["id_item"]
    try:
        todo[id_item]
        request.form["id_item"]
    except KeyError:
        return
    

if __name__ == '__main__':
   app.run(debug = True)