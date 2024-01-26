# No necesitas este archivo para la página web, ya que el código Python se convierte a JavaScript en el archivo script.js.
# Aquí está el código Python para referencia:
from turtle import *
from colorsys import *

def draw_turtle_pattern():
    bgcolor('black')
    speed(0)
    h = 0

    for i in range(371):
        c = hsv_to_rgb(h, 1, 1)
        h += 0.005
        color(c)
        circle(-i * 0.68, 200)
        right(80)

    done()

def hsv_to_rgb(h, s, v):
    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    mod = i % 6
    r = [v, q, p, p, t, v][mod]
    g = [t, v, v, q, p, p][mod]
    b = [p, p, t, v, v, q][mod]
    return r, g, b

# Llama a la función para dibujar el patrón Turtle cuando se ejecute este script directamente
if __name__ == "__main__":
    draw_turtle_pattern()

