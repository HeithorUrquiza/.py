print(' *** Pagamento Semanal Total ***')
sal = float(input("\nInforme o salário por hora: "))
hr = int(input("Horas regulares: "))
hrEx = int(input("Horas extras: "))

payHrEx = float(hrEx * (1.5 * sal))
payTot = float(sal * hr + payHrEx)

print(f"\nO pagamento semanal total será de R${round(payTot, 2)}")