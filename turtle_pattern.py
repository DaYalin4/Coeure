# No necesitas este archivo para la página web, ya que el código Python se convierte a JavaScript en el archivo script.js.
# Aquí está el código Python para referencia:
from turtle import *
from colorsys import *

bgcolor('black')
speed(0)
h=0

for i in range(371):
    c=hsv_to_rgb(h,1,1)
    h+=0.005
    color(c)
    circle(-i*0.68,200)
    right(80)

done()

