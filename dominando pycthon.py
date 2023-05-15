class Caneca:
    formato = 'cilindro com alça lateral'
    def __int__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'cheia'

    def beber(self):
        self.status = 'vazia'

    def encher(self):
        self.status = 'cheia'


class CanecaLondrina(Caneca):
    def  __int__(self):
        self.nome = 'caneca londrina'
        self.logo = 'cidade de londres'
        self.cor = 'amarelo'
        self.status = 'cheia'

caneca1= CanecaLondrina()
#caneca1= Caneca('barby', 'cidade londres','yellow')
caneca2= Caneca('yellow', 'cidade paris','amarelo')

print('')
print('')

caneca1.beber()
caneca1.encher()

caneca2.beber()

print('a caneca 1:', caneca1.status)
print('a caneca 2:', caneca2.status)

print(caneca1.formato)
