import random
#entradas
cotacao = float(input('Cotação atual do dólar: '))
#processamento
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)
print(f'Variação simulada: {variacao:.3%}')
print(f'Nova cotação: R${nova_cotacao:.4f}')
