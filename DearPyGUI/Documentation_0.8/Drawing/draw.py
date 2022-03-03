from dearpygui.core import *
from dearpygui.simple import *

def on_render(sender, data):
    clear_drawing("Drawing_1")
    counter = get_data("counter")
    counter += 1
    modifier = get_data("modifier")
    if counter < 300:
        modifier += 1
    elif counter < 600:
        modifier -= 1
    else:
        counter = 0
        modifier = 2

    xpos = 15 + modifier*1.25
    ypos = 15 + modifier*1.25
    color1 = 255 - modifier*.8
    color3 = 255 - modifier*.3
    color2 = 255 - modifier*.8
    radius = 15 + modifier/2
    segments = round(35-modifier/10)
    draw_circle("Drawing_1", [xpos, ypos], radius, [color1, color3, color2, 255], segments=segments, tag="circle##dynamic")
    add_data("counter", counter)
    add_data("modifier", modifier)

add_data("counter", 0)
add_data("modifier", 2)

with window("Tutorial"):
    add_drawing("Drawing_1", width=700, height=700)

set_render_callback(on_render)

start_dearpygui()