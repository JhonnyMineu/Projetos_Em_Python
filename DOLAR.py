import requests
from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()

cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
print(f'\nValor do dolar atualizado: {cotacao_dolar}')
print('\n<<<<<<<< Conversor de dolar >>>>>>>>>\n',
      '\nÚltima atualização:',(datetime.now()))


a1 = int(input('\nDigita o valor que quer converter: R$'))
b1 = (a1/float(cotacao_dolar))
c1 = "{:.2f}".format(b1)


print(f'\nO valor equivale a US{c1}')
print('\nObrigado por utilizar o código!  ;)')

