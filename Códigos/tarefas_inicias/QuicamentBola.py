print("\n *** Quicamento de uma Bola ***")

h = float(input("\nInforme a altura inicial da bola [m]: "))
indice = 0.6
dist = 0
kick = int(input("Quantas vezes acha que ela irá quicar? "))
for count in range(kick):
    dist += h
    h *= indice
    dist += h
print(f"\nA distância total percorrida foi de: {round(dist, 2)} m\n")
