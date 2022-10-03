import math

print(" *** Propriedades de uma Esfera ***")
r = float(input("\nInforme o raio da esfera: "))
D = float(r * 2)
circ = float(math.pi * D)
Ase = float(4 * math.pi * math.pow(r, 2))
Ve = float((4/3) * math.pi * math.pow(r, 3))

print(f"""\nResultado
---------
Diâmetro: {round(D, 2)}
Circunferência: {round(circ, 2)}
Área da Superfície: {round(Ase, 2)}
Volume: {round(Ve, 2)}""")
