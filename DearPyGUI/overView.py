# dearpygui.core contains the core functionality of Dear PyGui. Everything else is built on top of core.
from dearpygui.core import *

# dearpygui.simple contains simple wrappers and other utilities created from core to provide a more pleasant interface to DPG. As your code complexity grows its recommended to start using the simple module when applicable.
from dearpygui.simple import *


set_main_window_size(800, 800)

show_about()
show_documentation()

# when running this code please look at the about window and it will report which version of Dear PyGUI is running
start_dearpygui() 