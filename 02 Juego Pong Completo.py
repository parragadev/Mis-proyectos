import turtle

# Función para obtener el nombre y el color del jugador
def obtener_datos_jugador(numero_jugador):
    while True:
        nombre = input(f"Ingrese el nombre del jugador {numero_jugador}: ").strip()
        if nombre:
            break
        print("Nombre no válido. Por favor, ingrese un nombre válido.")
    while True:
        color = input(f"Ingrese el color de la paleta del jugador {numero_jugador} (ejemplo: blue, red, green): ").lower().strip()
        if color in ["blue", "red", "green", "yellow", "orange", "purple", "white"]:
            break
        print("Color no válido. Por favor, elija uno de los siguientes colores: blue, red, green, yellow, orange, purple, white")
    return nombre, color

# Ventana de Juego
ventana = turtle.Screen()
ventana.title("Bienvenido al juego del Pong desarrollado por Python")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Obtener datos del jugador 1
nombre_jugador1, color_jugador1 = obtener_datos_jugador(1)

# Obtener datos del jugador 2
nombre_jugador2, color_jugador2 = obtener_datos_jugador(2)

# Marcador del juego
marcadorA = 0
marcadorB = 0

# Jugador 1
jugador1 = turtle.Turtle()
jugador1.speed(0)
jugador1.shape("square")
jugador1.color(color_jugador1)
jugador1.penup()
jugador1.goto(-350, 0)
jugador1.shapesize(stretch_wid=5, stretch_len=1)

# Jugador 2
jugador2 = turtle.Turtle()
jugador2.speed(0)
jugador2.shape("square")
jugador2.color(color_jugador2)
jugador2.penup()
jugador2.goto(350, 0)
jugador2.shapesize(stretch_wid=5, stretch_len=1)

# Aspecto y tamaño de la pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("blue")
pelota.penup()
pelota.goto(0, 0)

# Para modificar la velocidad de la pelota
pelota.dx = 0.05
pelota.dy = 0.05

# Estilo del marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("yellow")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write(f"{nombre_jugador1}: 0           {nombre_jugador2}: 0", align="center", font=("Courier", 25, "normal"))

# Funciones
def jugador1_up():
    y = jugador1.ycor()
    y = y + 20
    jugador1.sety(y)

def jugador1_down():
    y = jugador1.ycor()
    y = y - 20
    jugador1.sety(y)

def jugador2_up():
    y = jugador2.ycor()
    y = y + 20
    jugador2.sety(y)

def jugador2_down():
    y = jugador2.ycor()
    y = y - 20
    jugador2.sety(y)

# Botones de movimiento en el teclado
ventana.listen()
ventana.onkeypress(jugador1_up, "w")
ventana.onkeypress(jugador1_down, "s")
ventana.onkeypress(jugador2_up, "Up")
ventana.onkeypress(jugador2_down, "Down")

while True:
    ventana.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Revision de colosiones con los bordes de la ventana
    if pelota.ycor() > 290:
        pelota.dy = pelota.dy * -1
    if pelota.ycor() < -290:
        pelota.dy = pelota.dy * -1

    # Si la pelota sale por la izquierda o derecha, esta regresa al centro.
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx = pelota.dx * -1
        marcadorA = marcadorA + 1
        marcador.clear()

        marcador.write(f"{nombre_jugador1}: {marcadorA}           {nombre_jugador2}: {marcadorB}", align="center", font=("Courier", 25, "normal"))
    
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx = pelota.dx * -1
        marcadorB = marcadorB + 1
        marcador.clear()
        marcador.write(f"{nombre_jugador1}: {marcadorA}           {nombre_jugador2}: {marcadorB}", align="center", font=("Courier", 25, "normal"))

    # Revision de colisiones
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugador2.ycor() + 50
            and pelota.ycor() > jugador2.ycor() - 50)):
        pelota.dx = pelota.dx * -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugador1.ycor() + 50
            and pelota.ycor() > jugador1.ycor() - 50)):
        pelota.dx = pelota.dx * -1