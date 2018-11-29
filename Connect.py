from flask import Flask, redirect, url_for, request, Response
from Controller import Controller
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
        controller = Controller()
        controller.adicionarGrupo()
        controller.adicionarUsuario()
        controller.adicionarTarefa()
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