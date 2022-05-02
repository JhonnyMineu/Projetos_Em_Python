import random
(\n '************************** Jogo da Forca ************************' \n)

tabuleiro = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

    +----+
    |    |
    |
    |
    |
    |
=========''','''
         
    +----+
    |    |
    |    O
    |
    |
    |
=========''','''
         
    +----+
    |    |
    |    O
    |    |
    |
    |
=========''','''
         
    +----+
    |    |
    |    O
    |    |\
    |
    |
=========''','''
         
    +----+
    |    |
    |    O
    |   /|\
    |
    |
=========''', '''
         
    +----+
    |    |
    |    O
    |   /|\
    |   /
    |
=========''','''
         
    +----+
    |    |
    |    O
    |   /|\
    |   / \
    |
=========''']

tentativa_letra = input('Digite uma letra')

def palavra_forca():
    with open("palavras.txt", "rt") as f:
        banco = f.readlines()
    return banco[random.randint(0, len(bank))].strip()



class forca:
    def __init__(self,palavra):
        self.palavra = palavra

    def adivinhar(self,):

    def fim_de_jogo(self):

    def jogo_ganho(self):

    def palavra_oculta(self):

    def status_game(self):


