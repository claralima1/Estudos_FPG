import turtle
#Para criar o quadro e a caneta:
q =  turtle.Screen() #Quadro
c = turtle.Turtle() #Caneta
c.shape('turtle') #para deixar a caneta em formato de tartaruga

#Para mover a caneta para frente:
c.forward(100)
#para mover a caneta  para trás:
c.backward(50)

#Para movimentar a tartaruga para outras direções:
c.right(90) #(usa-se ângulos)
c.left(90)
c.clear()

#criando o formato de um presente:
c.right(90)
c.forward(100)
c.right(90)
c.forward(80)
c.right(90)
c.forward(100)
c.left(90)
c.forward(10)
c.right(90)
c.forward(20)
c.right(90)
c.forward(100)
c.right(90)
c.forward(20)
c.right(90)
c.forward(90)
c.backward(36)
c.left(90)
c.forward(100)
c.left(90)
c.forward(10)
c.left(90)
c.forward(100)
c.left(320)
c.circle(10)
c.forward(40)
c.left(100)
c.forward(20)
c.left(100)
c.forward(30)
c.left(50)
#Para mover a tartaruga para qualquer ponto cartesiano
#c.goto(x,y)
#para voltar para o ponto de origem:
#c.home()
#para não encostar a caneta no papel:
#c.penup()
#para encostar a caneta do papel]:
#c.pendown()
#fazer um ponto:
#c.dot()

