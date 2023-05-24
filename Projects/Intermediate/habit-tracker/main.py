import requests
import datetime

#Criando um usuário
pixela_endpoint = "https://pixe.la/v1/users"
USER = "heith0r"
TOKEN = "Q!)s+mz*2cxBc8"

USER_PARAMS = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
} 

#resp = requests.post(url=pixela_endpoint, json=USER_PARAMS)
#print(resp.text)


#Criando um gráfico
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#resp = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(resp.text)


#Atualizando um gráfico
graph_update = {
    "color": "ajisai"
}

#resp = requests.put(f"{pixela_endpoint}/{USER}/graphs/graph1", json=graph_update, headers=headers)
#print(resp.text)


#Postando um pixels no gráfico
pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/graph1"

commit_graph = {
    "date":"20230524",
    "quantity":"30"
}

resp = requests.post(url=pixel_endpoint, json=commit_graph, headers=headers)
print(resp.text)