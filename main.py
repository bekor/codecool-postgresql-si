# this is the main part
import sys
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
print(current_file_path)
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/ui.py").load_module()
# Menu module
menu = SourceFileLoader("menu", current_file_path + "/menu.py").load_module()
# queries
queries = SourceFileLoader("queries", current_file_path + "/handle_queries.py").load_module()


def choose():
    inputs = ui.get_inputs(["Please choose an options"], "")
    option = inputs[0]
    if option == "1":
        queries.get_names_from_table()
    if option == "2":
        queries.get_nicnames_from_miskolc()
    if option == "3":
        queries.get_name_and_phone_by_firstname()
    if option == "4":
        queries.get_name_and_phone_by_email()
    if option == "5":
        queries.insert_data()
        queries.get_applicant_by_code()
    if option == "6":
        queries.update_data()
        queries.get_applicant_by_name()
    if option == "7":
        queries.delete_applicant()
        queries.all_applicants()
    if option == "8":
        queries.all_applicants()
    if option == "9":
        queries.all_mentors()
    if option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def main():
    while True:
        options_list = ["Mentor Names", "Mentors nick's in Miskolc", "Get Carol phone and name",\
                        "Get phone and name by email", "Insert new applicant", "Update applicant",\
                        "Delete applicant by email", "List all applicant", "List all mentor"]
        menu.handle_menu("Main menu", options_list, "Exit program")
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()