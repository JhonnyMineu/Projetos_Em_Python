n = 0

while n >= 0:
    n = int(input('A tabuada de qual número você quer ver agora?: '))
    if n <0:
        break
    for item in range(1,11):
        print(f' {n} x {item} = {item * n}')
print('Fim do programa. \nMUITO OBRIGADO!')