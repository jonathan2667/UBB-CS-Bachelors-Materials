
#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import functions
import constants
import copy
from constants import COMMAND, VALUE_APPARTMENT, VALUE_UTILITIES_TO_CHANGE, INDEX_ABOVE_TO_REMOVE_EXPENSES, CONDITION_REMOVE

def get_input_user(list_of_appartments):
    #list_of_appartments = functions.build_list_appartments_with_0_amount_and_0_utilities(list_of_appartments)
    list_of_appartments = functions.randomize_list_of_tenants(list_of_appartments)
    functions.clean_history_of_modification_list()
    functions.update_history_of_modification_list(list_of_appartments)

    while True:
        answer_from_user = input("Choose From The Menu!\n")
        splitted_answer_from_user = answer_from_user.split()

        try:
            if splitted_answer_from_user[COMMAND] == 'add':
                try:
                    list_of_appartments = functions.add_new_transaction(splitted_answer_from_user[VALUE_APPARTMENT],
                                                                        splitted_answer_from_user[VALUE_UTILITIES_TO_CHANGE],
                                                                        splitted_answer_from_user[INDEX_ABOVE_TO_REMOVE_EXPENSES], list_of_appartments)
                    print_menu()
                except Exception as ex:
                    print(ex)
            elif splitted_answer_from_user[COMMAND] == 'remove':
                try:
                    functions.remove_expenses_menu(splitted_answer_from_user, list_of_appartments)
                    print_menu()
                except Exception as ex:
                    print(ex)
            elif splitted_answer_from_user[COMMAND] == 'replace':
                try:
                    functions.replace_appartment_menu(splitted_answer_from_user, list_of_appartments)
                    print_menu()
                except Exception as ex:
                    print(ex)
            elif splitted_answer_from_user[COMMAND] == 'list':
                list_menu_appartments(splitted_answer_from_user, list_of_appartments)
            elif splitted_answer_from_user[COMMAND] == 'filter':
                try:
                    functions.filter_appartment_menu(splitted_answer_from_user, list_of_appartments)
                    print_menu()
                except Exception as ex:
                    print(ex)
            elif splitted_answer_from_user[COMMAND] == 'undo':
                try:
                    list_of_appartments = functions.undo_operation_menu(list_of_appartments)
                    print_menu()
                except Exception as ex:
                    print(ex)
            elif splitted_answer_from_user[COMMAND] == 'exit':
                break
        except Exception as ex:
            print(str(ex) + "tryUI")

def print_menu():
    print("This is the menu, Jane!")
    print("""
        - (A) Add new transaction
            - add <apartment> <type> <amount> (type (from one of the predefined categories water, heating, electricity, gas and other)
        - (B) Modify expenses
            - remove <apartment>
            - remove <start apartment> to <end apartment>
            - remove <type>
            - replace <apartment> <type> with <amount>
        - (C) Display expenses having different properties
            - list
            - list <apartment>
            - list [ < | = | > ] <amount>
        - (D) Filter
            - filter <type>
            - filter <value>
        - (E) Undo
            - undo
    """)


""" C - LIST expenses having different properties"""
"""
list – display all expenses
list 15 – display all expenses for apartment 15
list > 100 - display all apartments having total expenses >100 RON
list = 17 - display all apartments having total expenses =17 RON
"""

def display_list(list):
    for index in list:
        print(index)

def  display_appartments_with_expanses_over_give_number(value_not_to_get_over_for_expenses, list_of_appartments):
    for appartment in list_of_appartments:
        if functions.get_sum_expenses(appartment) > value_not_to_get_over_for_expenses:
            print(appartment)

def display_appartments_with_expanses_equal_with_give_number(reference_value_for_comparation_utilities_expenses, list_of_appartments):
    for appartment in list_of_appartments:
        if functions.get_sum_expenses(appartment) == reference_value_for_comparation_utilities_expenses:
            print(appartment)

def list_menu_appartments(splitted_answer_from_user, list_of_appartments):
    if len(splitted_answer_from_user) == VALUE_APPARTMENT:
        display_list(list_of_appartments)
    elif len(splitted_answer_from_user) == CONDITION_REMOVE:
        try:
            reference_value_for_comparation_utilities_expenses = int(splitted_answer_from_user[VALUE_APPARTMENT])
        except ValueError:
            raise("VALUE ERROR INT CONVERSION")
        else:
            print(list_of_appartments[reference_value_for_comparation_utilities_expenses])
    elif len(splitted_answer_from_user) == INDEX_ABOVE_TO_REMOVE_EXPENSES:
        try:
            reference_value_for_comparation_utilities_expenses = int(splitted_answer_from_user[VALUE_UTILITIES_TO_CHANGE])
        except ValueError:
            raise("VALUE ERROR INT CONVERSION")
        else:
            if splitted_answer_from_user[VALUE_APPARTMENT] == '>':
                display_appartments_with_expanses_over_give_number(reference_value_for_comparation_utilities_expenses, list_of_appartments)
            elif splitted_answer_from_user[VALUE_APPARTMENT] == '=':
                display_appartments_with_expanses_equal_with_give_number(reference_value_for_comparation_utilities_expenses, list_of_appartments)