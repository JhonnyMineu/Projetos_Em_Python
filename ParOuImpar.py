from random import randint

print('-='*15)
print('Vamos jogar PAR ou IMPAR')
print('-='*15)

numero = int(input('\nEscolha um número: '))
escolha = str(input('\nVocê quer par ou impar? [P/I]: ')).strip().upper()[0]
vitorias = 0
cpu = randint(0,10)

while vitorias >= 0:
    soma = numero + cpu
    if soma %2 == 0 and escolha == 'P':
        print(f'O computador escolheu {cpu} e você {numero} que deu PAR. Então você ganhou!')
        vitorias += 1
        print(f'<<<<<<< Vitorias consecutivas: {vitorias} >>>>>>>>')
    elif soma %2 != 0 and escolha == 'I':
        print(f'O computador escolheu {cpu} e você {numero} que deu IMPAR. Então você ganhou!')
        vitorias += 1
        print(f'<<<<<<< Vitorias consecutivas: {vitorias} >>>>>>>>')
    elif soma % 2 == 0 and escolha == 'I':
        print(f'O computador escolheu {cpu} e você {numero} que deu PAR. Então COMPUTADOR ganhou!')
        vitorias = -1
        break
    elif soma % 2 != 0 and escolha == 'P':
        print(f'O computador escolheu {cpu} e você {numero} que deu IMPAR. Então COMPUTADOR ganhou!')
        vitorias = -1
        break

    numero = int(input('\nEscolha um número: '))
    escolha = str(input('\nVocê quer par ou impar? [P/I]: ')).strip().upper()[0]
print('\nObrigado por jogar. Até mais')