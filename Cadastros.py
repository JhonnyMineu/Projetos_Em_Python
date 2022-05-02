print('-='*15)
print('Cadastro de Pessoas')
print('-='*15)

idade = int(input('IDADE: '))
sexo = str(input('SEXO [F/M]: ')).strip().upper()[0]

continuar = ''
contagem = 0
cont_idade = 0
cont_masc = 0
cont_fem = 0

while continuar != 'N':
    continuar = str(input('Você deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]
    if continuar == 'S':
        idade = int(input('IDADE: '))
        sexo = str(input('SEXO [F/M]: ')).strip().upper()[0]
        contagem += 1
    if continuar not in 'SN':
        continuar = str(input('Você deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
       cont_masc += 1
    if sexo == 'F' and idade < 20:
        cont_fem += 1
    if continuar == 'N':
        print('Fim do programa. \n Abaixo seguem as estatisticas:')
        break
    if sexo not in 'MF':
        sexo = str(input('SEXO [F/M]: ')).strip().upper()[0]

print(f'\n Temos {cont_idade} pessoas maiores de 18 anos. Temos {cont_masc} homens. Por fim, temos {cont_fem} mulheres com menos de 20 anos')


