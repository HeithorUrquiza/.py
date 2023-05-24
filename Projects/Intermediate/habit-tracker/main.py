import requests
import datetime as df
import os
from dotenv import load_dotenv

load_dotenv()

#Criando um usuário
pixela_endpoint = "https://pixe.la/v1/users"
USER = os.getenv("USER")
TOKEN = os.getenv("TOKEN")

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

today = df.datetime.now()

commit_graph = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"30"
}

#resp = requests.post(url=pixel_endpoint, json=commit_graph, headers=headers)
#print(resp.text) 


#Atualizando um pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USER}/graphs/graph1/20230224"

update_pixels = {
    "quantity":"120"
}

#resp = requests.put(url=pixel_update_endpoint, json=update_pixels, headers=headers)
#print(resp.text)


#Deletando um pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USER}/graphs/graph1/20230224"

resp = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(resp.text)