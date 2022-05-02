from random import randint
print('\33[34m<<<<<<<<<<< JO KEN PO >>>>>>>>>>>>\33[m')
print('\nEscolha uma das opções: \n1* PEDRA;\n2* PAPEL;\n3* TESOURA.')
a1 = int(input('\nDigite o número da opção que escolheu: '))
a2 = randint(1,3)

b1 = {1: 'Pedra',2:'Papel',3:'Tesoura'}
print(f'\nEu escolhi: {b1[a2]}')

if a1 == 1 and a2 == 3:
    print('\nPedra ganha de Tesoura, então você ganhou. PARABÉNS!')
elif a1 == 1 and a2 == 2:
    print('\nPedra perde de Papel, então eu venci!')
elif a1 == 1 and a2 == 1:
    print('\nEu também joguei Pedra. EMPATAMOS')
elif a1 == 2 and a2 == 1:
    print('\nPedra perde de Papel, então você ganhou. PARABÉNS!')
elif a1 == 2 and a2 == 3:
    print('\nPapel perde de Tesoura, então você ganhou. PARABÈNS!')
elif a1 == 2 and a2 ==2:
    print('\nEu também joguem Papel. EMPATAMOS')
elif a1 == 3 and a2 == 1:
    print('\nPedra ganha de Tesoura, então eu venci!')
elif a1 == 3 and a2 == 2:
    print('\nPapel perde de Tesoura, então eu venci!')
elif a1 == 3 and a2 == 3:
    print('\nEu também joguei Tesoura. EMPATAMOS')
else:
    print('\nOpção inválida. Comece de novo!')