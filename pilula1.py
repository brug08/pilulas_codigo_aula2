import math
#entradas
assinantes = int(input('Assinantes atuais: '))
mensalidade = float(input('Valor da mensalidade: '))
taxa = float(input('Taxa de crescimento mensal (%): '))/100
meses = int(input('Meses de projeção: '))
#processamento
assinantes_finais = assinantes * math.pow((1+taxa), meses)
receita_final = assinantes_finais * mensalidade
#saida
print(f'Assinantes estimados: {assinantes_finais:.0f}')
print(f'Receita mensal estimada: {receita_final:.2f}')
