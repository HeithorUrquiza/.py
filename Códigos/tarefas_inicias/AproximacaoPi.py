from math import pi

print("\n --- APROXIMÇÃO DE PI ---")

piPorQuatro = 0
numerador = 1
denominador = 1

n = int(input("\nInsira o número de iterações para a aproximação: "))

for count in range(n):
    piPorQuatro += numerador/denominador
    numerador = (-numerador)
    denominador += 2
print(f"A aproximação para PI é: {piPorQuatro * 4}")
print("Valor convencional de PI: {}".format(pi))



