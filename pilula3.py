import datetime
#entrada
data_compra = input('Digite a data da compra d/m/aaaa: ')
meses = int(input('Prazo de garantia: '))
#Processamento
data_incial = datetime.datetime.strptime(data_compra, '%d/%m/%Y')
data_final = data_incial + datetime.timedelta(days=meses * 30)
#saida
print(f'Garantia válida até {data_final.strftime('%d/%m/%Y')}')
print(f'Dia da semana: {data_final.strftime('%A')}')
