galera = []
contagem = 0
while True:
    nome = str(input('Digite o nome: '))
    peso = int(input('Digite o peso: '))
    individuo = [nome,peso]
    galera.append(individuo)
    contagem += 1

    continuar = str(input('\nQuer continuar adicionando pessoas? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('\nFim da coleta de dados!')
        break
    if continuar not in 'SN':
        print('\nResposta inválida. Tente novamente: ')
        continuar = str(input('\nQuer continuar adicionando pessoas? [S/N]: ')).strip().upper()[0]

print(galera)
print(f'Foram cadastradas {contagem} pessoas')
