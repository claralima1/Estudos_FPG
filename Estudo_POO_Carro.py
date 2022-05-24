
class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        print('Carro ligado')
    
    def Dirigir(self):
        print('Carro em movimento')
    
    def Desligar(self):
        print('Carro Desligado')

    def ExibirInformaçõesDoCarro(self):
        print(self.marca, self.ano, self.cor)
    
carro1 = Carro('Fiat', '2003', 'Preto')
carro1.ligar()
carro1.Dirigir()
carro1.Desligar()
carro1.ExibirInformaçõesDoCarro()
