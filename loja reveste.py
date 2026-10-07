print("sistema de vendas")
print("loja reveste")

continuar = "sim"
total_dia = 0
 

while continuar == "sim":

# venda da loja reveste



 produto = input("digite o nome do produto")
 preço = int(input("digite o preço do produto"))
 quantidade = int(input("digite a quantidade do produto")) 
 total = preço * quantidade 

 print("produto:",produto)
 print(f"total da venda: R$ {total:.2f}")
 print("quantidade:",quantidade)

#resto da venda da loja resveste
 continuar = input("deseja continuar a compra? (sim/nao): ")

desconto_= float(input("qual valor do desconto ??"))
valor_desconto = total * (desconto_/100)
total_final = total - valor_desconto
total_dia =  total_dia + total_final
print(f"total final: R$ {total_final:.2f}")



 
#formas de pagamentos da loja reveste 
outro_pagamento = input("qual seria a outra forma de pagamento (pix/boleto/cartao debito/cartao credito/dinehiro): ")
while outro_pagamento == "sim":

 pagamento = input("digite a forma de pagamento (dinheiro,pix,cartao de credito,cartao de debito, boleto): ")
 print(f"forma de pagamento escolhida: {pagamento}")

# formas da envio da loja resvete 

envio = input("digite a formas de envio (correios, trasportadora, motoboy,retirrada na loja:)")

print(f"forma de envio escolhida: {envio}")




#fechamento da loja reveste no dia

dinheiro = float(input("total de dinheiro recebido no dia:"))
cartao_debito = float(input("total de cartao de debito recebido no dia:"))
pix  = float(input("total de pix recebido no dia:"))
cartao_de_credito = float(input("total recebido no cartao de credito no dia:"))
boleto = float(input("total de boleto recebido no dia:"))

total_dia = dinheiro + cartao_debito + pix + cartao_de_credito + boleto






print("contabilidade da loja reveste")

valor_entrada_por_dia = total_dia
dias = 31
total_mes = dias*valor_entrada_por_dia
print("valor total de lucro no mes",total_mes)

meses= 12

valor_total_de_lucro_no_ano = total_mes*meses
print("total de lucro no ano e de",valor_total_de_lucro_no_ano)

#despeja da loja

compra_de_mercadoria = float(input("qual valor da mercadoria"))
embalagem_e_sacola =   float(input("valor da embalagem e sacola?"))
total_despesa = compra_de_mercadoria + embalagem_e_sacola
print("total de despesa da loja",total_despesa*meses)

#valor de lucro da loja no ano com as despesas 

valor_total_de_lucro_no_ano - total_despesa
print("o valor de lucro na loja reveste no  ano com as despesas e de",valor_total_de_lucro_no_ano - total_despesa)