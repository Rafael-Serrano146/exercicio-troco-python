lista_moedas = [1,5,10,25,50]
qtd_moedas = 0


troco = int(input("Digite o valor do pagamento até 99 centavos: "))


lista_moedas.sort(key=int, reverse=True)

for moeda in lista_moedas:
    qtd_moedas = troco // moeda
    if (qtd_moedas >= 1):
        print (f"{qtd_moedas} moeda(s) de {moeda} centavos")
        troco = troco % moeda