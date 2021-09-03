from dearpygui.core import *
from dearpygui.simple import *

def update_var(sender, data):
    my_var = get_value("Input Checkbox")
    log_debug(my_var)

show_logger() # were going to use the logger here to show the result

with window("Tutorial"):
    add_checkbox("Input Checkbox", callback=update_var)

start_dearpygui() 