import requests
import json

def main():
    id_item = input("Digite o id (por padrao retorna todos os itens): ")
    route = "http://127.0.0.1:5000/"
    if(id_item == ""):
        result = requests.get(route)
    else:
        route_adiciona = route + "adicionar"
    
        query = {}
        query["id_item"] = id_item
        query["dados"]  = id_item
        result = requests.post(route_adiciona, data = query)
    
    # routeBusca = route + "busca"

    # request = requests.get(routeBusca, data = query)
    body = result.content
    response_dict = body.decode("utf-8")
    print(json.loads(response_dict))

main()