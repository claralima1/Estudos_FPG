class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou Desligando')
    
    def exibirInformaçõesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)
    
computador1 = Computador('Sansung', '16GB', 'Nvidia')
computador1.ligar()
computador1.Desligar()
computador1.exibirInformaçõesDesteComputador()





