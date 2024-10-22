import turtle

# Configuração da janela
tela = turtle.Screen()
tela.title("Teste do jogo")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

# Pontuação
pontuacao_a = 0
pontuacao_b = 0

# Jogador A
jogador_a = turtle.Turtle()
jogador_a.speed(5)
jogador_a.shape("square")
jogador_a.color("white")
jogador_a.shapesize(stretch_wid=6, stretch_len=1)
jogador_a.penup()
jogador_a.goto(-350, 0)

# Jogador B
jogador_b = turtle.Turtle()
jogador_b.speed(5)
jogador_b.shape("square")
jogador_b.color("white")
jogador_b.shapesize(stretch_wid=6, stretch_len=1)
jogador_b.penup()
jogador_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(60)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = -0.2

# Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador A: 0  Jogador B: 0", align="center", font=("Courier", 24, "normal"))

# Funções
def jogador_a_sobe():
    y = jogador_a.ycor()
    y += 30
    jogador_a.sety(y)

def jogador_a_desce():
    y = jogador_a.ycor()
    y -= 30
    jogador_a.sety(y)

def jogador_b_sobe():
    y = jogador_b.ycor()
    y += 30
    jogador_b.sety(y)

def jogador_b_desce():
    y = jogador_b.ycor()
    y -= 30
    jogador_b.sety(y)

# Teclado
tela.listen()
tela.onkeypress(jogador_a_sobe, "w")
tela.onkeypress(jogador_a_desce, "s")
tela.onkeypress(jogador_b_sobe, "Up")
tela.onkeypress(jogador_b_desce, "Down")

# Loop principal

while True:
    tela.update()

    # Movendo a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Verificando colisão com a borda superior
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    # Verificando colisão com a borda inferior
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    # Verificando colisão com a borda direita
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontuacao_a += 1
        placar.clear()
        placar.write("Jogador A: {}  Jogador B: {}".format(pontuacao_a, pontuacao_b), align="center", font=("Courier", 24, "normal"))

    # Verificando colisão com a borda esquerda
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontuacao_b += 1
        placar.clear()
        placar.write("Jogador A: {}  Jogador B: {}".format(pontuacao_a, pontuacao_b), align="center", font=("Courier", 24, "normal"))

    # Verificando colisão com os jogadores
    if (bola.dx > 0 and bola.xcor() > 340 and bola.xcor() < 350 and bola.ycor() < jogador_b.ycor() + 50 and bola.ycor() > jogador_b.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1

    if (bola.dx < 0 and bola.xcor() < -340 and bola.xcor() > -350 and bola.ycor() < jogador_a.ycor() + 50 and bola.ycor() > jogador_a.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1

# Fechando a janela

tela.mainloop()