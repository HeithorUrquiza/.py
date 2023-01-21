import pandas as pd
import numpy as np

concursos = pd.read_csv('C:\\Users\\heith\\OneDrive\\Documentos\\GitHub\\Python_cods\\forfun\\BB\\concursos.csv', ';')

print(concursos.info()) #Informações sobre o DataFrame
print(concursos.head()) #Mostra os 5 primeiros elem por padrão tail() mostra os últimos 5

