"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import * #para importar a biblioteca Turtle

from freegames import vector # para importar para importar a biblioteca vector


def line(start, end): # método para determinar a posição inicial e fianl da caneta e desenhar uma linha
    "Draw line from start to end." 
    up() # para puxar a caneta para cima sem desenhar ao se mover
    goto(start.x, start.y) #método (par de cordenadas) (X- um número ou um par/vetor de números | y – um número ouNone)
    down() # para puxar a caneta para baixo, desenhando ao se mover
    goto(end.x, end.y)

def square(start, end): # método para determinar a posição inicial e final da caneta
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill() #Para ser chamado antes de desenhar uma forma a ser preenchida.

    for count in range(4): # função para desenhar um quadrado
        forward(end.x - start.x)
        left(90)

    end_fill() #Para Preencher a forma desenhada após a última chamada para begin_fill()


def circle(start, end): # método para desenhar um círculo inteiro
    "Draw circle from start to end."
    pass  # TODO
   


    
def rectangle(start, end): #método para desenhar um retângulo inteiro
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill() #Para ser chamado antes de desenhar uma forma a ser preenchida.

    for count in range(4): # função 
        forward(end.x - start.x)
        left(90)


def triangle(start, end): #método para desenhar um triângulo inteiro
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill() #Para ser chamado antes de desenhar uma forma a ser preenchida.

    for count in range(3): # função para desenhar o triângulo
        forward(end.x - start.x)
        left(120)


def tap(x, y): # método para armazenar o ponto de partida
    "Store starting point or draw shape."
    start = state['start']
    

    if start is None: # estrutura condicional | se o estado inicial da tartaruga for 'NONE" (vazio):
        state['start'] = vector(x, y) # estado inicial da tartaruga = vetor(x,y)
    else:
        shape = state['shape'] 
        end = vector(x, y) 
        shape(start, end)
        state['start'] = None
        


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)

listen()

onkey(undo, 'u') #borracha ("controlZ")
onkey(lambda: color('black'), 'K')#botão para mudar de cor
onkey(lambda: color('white'), 'W')#botão para mudar de cor
onkey(lambda: color('green'), 'G')#botão para mudar de cor
onkey(lambda: color('blue'), 'B')#botão para mudar de cor
onkey(lambda: color('red'), 'R')#botão para mudar de cor
onkey(lambda: color('purple'), 'P')#botão para mudar de cor
onkey(lambda: store('shape', line), 'l')#botão para fazer uma linha
onkey(lambda: store('shape', square), 's')#botão para fazer um quadrado
onkey(lambda: store('shape', circle), 'c')#botão para fazer uum circulo
onkey(lambda: store('shape', rectangle), 'r')#botão para fazer um retângulo
onkey(lambda: store('shape', triangle), 't')#botão para fazer um triângulo
done()

