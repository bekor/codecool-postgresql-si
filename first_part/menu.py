import os
import sys
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/ui.py").load_module()


def handle_menu(title, options_list, exit_message):
    ui.print_menu(title, options_list, exit_message)


def choose(option_list):
    inputs = ui.get_inputs(["Please choose an options"], "")
    option = inputs[0]
    for i, opts in enumerate(option_list):
        if option == str(i+1):
            opts()
    if option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")