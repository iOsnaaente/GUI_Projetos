from dearpygui.core import *
from dearpygui.simple import *

with window("Tutorial"):
    add_text("First created widget")
    add_text("This is some text on window 2", parent="window 2")  # we can even specify the parent before it was created
    add_text("This is some text on child 1", parent="child 1")

with window("window 1"):
    with child("child 1"):
        add_checkbox("Checkbox")                              # this is a input item added inside of the child

add_checkbox("Last created widget", parent="MainWindow", before="First created widget")
add_checkbox("Last created widget 2", parent="child 1", before="Checkbox")

# empty window
with window("window 3"): # simple
    pass

start_dearpygui()