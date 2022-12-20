
taxJurosAnual = 0.12
taxJuroMensal = taxJurosAnual/12

precoCompra = float(input("Informe o preço de compra: R$"))
precoInicial = precoCompra * 0.1
pagMensal = (precoCompra - precoInicial) * 0.05
mes = 1
saldoTot = precoCompra - precoInicial


print("\n Mês   Saldo total atual devido   Juros do mês   Valor devido do mês   Pagamento do mês   Saldo remanescente ")

while saldoTot > 0:
    if (pagMensal > saldoTot):
        valuePrince = saldoTot
        pag = saldoTot
        saldoRest = 0
    else:
        jurosMensal = saldoTot * taxJuroMensal
        valuePrince = pagMensal - jurosMensal
        pag = pagMensal + jurosMensal
        saldoRest = saldoTot - valuePrince
    print("%3d    R$%14.2f           R$%8.2f     R$%10.2f          R$%9.2f        R$%11.2f"
        %(mes, saldoTot, jurosMensal, valuePrince, pag, saldoRest))
    saldoTot = saldoRest
    mes += 1

