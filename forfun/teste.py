import numpy as np

anos_nascimento = np.loadtxt('C:\\Users\\heith\\OneDrive\\Documentos\\GitHub\\Python_cods\\forfun\\anos.txt')
idades = 2021 - anos_nascimento

media = idades.sum() / idades.size
print(media)
