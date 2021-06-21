import turtle


def desenhaquadrado(t, tam):
    """Faça a tartaruga t desenhar um quadrado de lado tam."""

    for i in range(8):
        t.forward(tam)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("Light green")

alex = turtle.Turtle()
desenhaquadrado(alex, 50)

wn.exitonclick()
