primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))

print('<<<<<<<<<<<<< OPÇÕES >>>>>>>>>>>>>>')
print('''\n* 1 - SOMAR\n* 2 - MULTIPLICAR\n* 3 - MAIOR\n* 4 - NOVOS NÚMEROS\n* 5 - SAIR DO PROGRAMA''')

opcao = int(input('\nSelecione uma das opções acima: '))

while opcao != 5:
    if opcao > 5:
        opcao = int(input('\nOpção selecionada inválida, por favor digite uma opção válida: '))

    if opcao == 1:
        a1 = primeiro + segundo
        print(f'\nVocê escolheu a opçao "SOMAR", o resultado é: {a1}')
        opcao = 5

    if opcao == 2:
        a2 = primeiro * segundo
        print(f'\nVocê escolheu a opção "MULTIPLICAR", o resultado é: {a2}')
        opcao = 5

    if opcao == 3:
        print(f'\nVocê escolheu a opção "MAIOR", o maior número é: {max(primeiro, segundo)}')
        opcao = 5

    if opcao == 4:
        primeiro = int(input('\nDigite um número: '))
        segundo = int(input('\nDigite outro número: '))
        opcao = int(input('\nSelecione uma das opções acima: '))


    if opcao == 5:
        print('\nAté mais!')
        pass


print('\nACABOU')