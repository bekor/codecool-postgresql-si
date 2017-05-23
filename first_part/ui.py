from terminaltables import SingleTable
import os
from textwrap import wrap
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))


# This function needs to print outputs like this:
#
# @table_it: list of tuple - the table to print out with title
def print_table(data_table):
    data_table = [list(data) for data in data_table]
    max_width = get_table_elements_length(data_table)  # reduce the width of the columns
    for i, row in enumerate(data_table):
        for k, col in enumerate(row):
            if len(str(col)) > max_width[k]:
                wrapped_string = '\n'.join(wrap(col, max_width))
                row[k] = wrapped_string
    table = SingleTable(data_table)
    table.inner_heading_row_border = True
    table.inner_row_border = True
    print(table.table)


# This function needs to generate outputs like this:
# Main menu:
# (1) Actual Season
# (2) New Season
# (3) Plants
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):  # ready to use
    numbers = [str(i+1) for i in range(len(list_options))]
    print(title + ":")
    for pos, option in enumerate(list_options):
        print("(" + numbers[pos] + ") " + option)
    print("(0) " + exit_message)


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    print("\n" + label)
    print(result + "\n")

    
# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    print(title)
    if len(list_labels) < 2:
        return input(list_labels[0] + ": ")
    else:
        inputs = []
        for items in list_labels:
            inputs.append(input(items + ": "))
        return inputs


# return the max length of the longest element from every column
#
# @table: list of list
def get_table_elements_length(table):
    colum_max_lens = []
    for i in range(len(table[0])):
        colum_max_lens.append(len(str(max(table, key=lambda x: len(str(x[i])))[i])))
    return colum_max_lens


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    print("Error: " + str(message))