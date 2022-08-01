import turtle

def desenhar(ang, tam, qtd_lados):
    for c in range(qtd_lados):
        desenhista.forward(tam) #ir para frente
        desenhista.left(ang) #virar para a esquerda
    

num_lados = int(input("Digite o número de lados: "))
angulo = 360/num_lados
tela= turtle.Screen() #Para criar a tela
tela.bgcolor('#87CEFA') #cor da tela
desenhista= turtle.Turtle() #para chamar todas a funções a biblioteca

desenhar(angulo, 100,num_lados) #passar os parâmetros

tela.exitonclick() #Fazer a tela sair apenas com clik

