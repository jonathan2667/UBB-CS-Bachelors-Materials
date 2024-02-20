##
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import copy
import random
from constants import COMMAND, VALUE_APPARTMENT, VALUE_UTILITIES_TO_CHANGE, INDEX_ABOVE_TO_REMOVE_EXPENSES, VALUE_TO_REPLACE_UTILITIES, NUMBER_APPARTMENTS, CONDITION_REMOVE, REPLACE_CONDITION, CONDITION_REMOVE_SPECIFIC_APPARTMENT

history_of_modification_lists = []

def build_list_appartments_with_default_amount_and_default_utilities(list_of_appartments):
    for i in range(0, NUMBER_APPARTMENTS):
        tenant = {
            "apartment": i,
            "amount": 0,
            "utilities": {
                "water": 0,
                "heating": 0,
                "electricity": 0,
                "gas": 0,
                "other": 0
            }
        }
        list_of_appartments.append(tenant)
    return list_of_appartments

def randomize_list_of_tenants(list_of_tenants):
    number_of_apartments = NUMBER_APPARTMENTS
    first_apartment_index = 0
    for i in range(0, number_of_apartments):
        tenant = {
            "apartment": first_apartment_index + i,
            "amount": 0,
            "utilities": {
                "water": random.randint(0, 200),
                "heating": random.randint(0, 200),
                "electricity": random.randint(0, 200),
                "gas": random.randint(0, 200),
                "other": random.randint(0, 200)
            }
        }
        tenant["amount"] = get_sum_expenses(tenant)
        # tenant_no_.append(first_index + i)
        list_of_tenants.append(tenant)
    return list_of_tenants

def clean_history_of_modification_list():
    global history_of_modification_lists
    history_of_modification_lists = []

def update_history_of_modification_list(list_of_tenants):
    global history_of_modification_lists
    history_of_modification_lists.append(copy.deepcopy(list_of_tenants))


"""
Setters
"""

def set_water(appartment, water):
    appartment["utilities"]["water"] = water
    return appartment

def set_heating(appartment, heating):
    appartment["utilities"]["heating"] = heating
    return appartment

def set_electricity(appartment, electricity):
    appartment["utilities"]["electricity"] = electricity
    return appartment

def set_gas(appartment, gas):
    appartment["utilities"]["gas"] = gas
    return appartment

def set_other(appartment, other):
    appartment["utilities"]["other"] = other
    return appartment

def set_amount(appartment, amount):
    appartment["amount"] = amount
    return appartment


"""
Getters
"""

def get_water(appartment):
    return appartment["utilities"]["water"]

def get_heating(appartment):
    return appartment["utilities"]["heating"]

def get_electricity(appartment):
    return appartment["utilities"]["electricity"]

def get_gas(appartment):
    return appartment["utilities"]["gas"]

def get_other(appartment):
    return appartment["utilities"]["other"]

def get_amount(appartment):
    return appartment["amount"]

def get_sum_expenses(appartment):
    sum_expenses = 0
    sum_expenses += appartment["utilities"]["water"]
    sum_expenses += appartment["utilities"]["heating"]
    sum_expenses += appartment["utilities"]["electricity"]
    sum_expenses += appartment["utilities"]["gas"]
    sum_expenses += appartment["utilities"]["other"]
    return sum_expenses

""" A - ADD TRANSACTION """

def add_new_transaction(appartment, transaction_type, amount, list_of_apparments):
    global history_of_modification_lists
    try:
        appartment = int(appartment)
        amount = int(amount)
        transaction_type == "water"
        transaction_type == "gas"
        transaction_type == "heating"
        transaction_type == "electricity"
        transaction_type == "other"
    except:
        raise ValueError("There should be an int")
        raise TypeError("Wrong transaction_type!")

    else:
        if transaction_type == "water":
            set_water(list_of_apparments[appartment], get_water(list_of_apparments[appartment]) + amount)
        elif transaction_type == "gas":
            set_gas(list_of_apparments[appartment], get_gas(list_of_apparments[appartment]) + amount)
        elif transaction_type == "heating":
            set_heating(list_of_apparments[appartment], get_heating(list_of_apparments[appartment]) + amount)
        elif transaction_type == "electricity":
            set_electricity(list_of_apparments[appartment], get_electricity(list_of_apparments[appartment]) + amount)
        elif transaction_type == "other":
            set_other(list_of_apparments[appartment], get_other(list_of_apparments[appartment]) + amount)
        history_of_modification_lists.append(copy.deepcopy(list_of_apparments))
        return list_of_apparments


""" B - REMOVE TRANSACTION

remove 15 – remove all expenses for apartment 15
remove 5 to 10 – remove all expenses for apartments between 5 and 10
remove gas – remove all gas expenses from all apartments
replace 12 gas with 200 – replace the amount of the expense with type gas for apartment 12 with 200 RON
"""

def remove_all_utilities_for_appartment(appartment):
    set_water(appartment, 0)
    set_gas(appartment, 0)
    set_heating(appartment, 0)
    set_electricity(appartment, 0)
    set_other(appartment, 0)

def remove_an_expense_type_of_utilities_for_all_appartments(list_of_appartments, expense_type):
    global history_of_modification_lists
    for i in range(NUMBER_APPARTMENTS):
        if expense_type == "water":
            set_water(list_of_appartments[i], 0)
        elif expense_type == "gas":
            set_gas(list_of_appartments[i], 0)
        elif expense_type == "heating":
            set_heating(list_of_appartments[i], 0)
        elif expense_type == "electricity":
            set_electricity(list_of_appartments[i], 0)
        elif expense_type == "other":
            set_other(list_of_appartments[i], 0)

def remove_expenses_menu(splitted_answer_from_user, list_of_appartments):
    global history_of_modification_lists
    if len(splitted_answer_from_user) == CONDITION_REMOVE:
        utilities = {'water', 'gas', 'electricity', 'heating', 'other'}
        if splitted_answer_from_user[VALUE_APPARTMENT] in utilities:
            remove_an_expense_type_of_utilities_for_all_appartments(list_of_appartments, splitted_answer_from_user[VALUE_APPARTMENT])
            history_of_modification_lists.append(copy.deepcopy(list_of_appartments))
        else:
            try:
                apparment_number = int(splitted_answer_from_user[VALUE_APPARTMENT])
                remove_all_utilities_for_appartment(list_of_appartments[apparment_number])
                history_of_modification_lists.append(copy.deepcopy(list_of_appartments))
            except Exception as ex:
                raise("VALLUE ERROR APPARTMENT NUMBER INT")

    elif len(splitted_answer_from_user) == CONDITION_REMOVE_SPECIFIC_APPARTMENT:
        try:
            first_number_input_to_remove_apparment_facilities_from = int(splitted_answer_from_user[VALUE_APPARTMENT])
            second_number_input_to_remove_apparment_facilities_from = int(splitted_answer_from_user[INDEX_ABOVE_TO_REMOVE_EXPENSES])
            for index in range(first_number_input_to_remove_apparment_facilities_from, second_number_input_to_remove_apparment_facilities_from + 1):
                remove_all_utilities_for_appartment(list_of_appartments[index])
            history_of_modification_lists.append(copy.deepcopy(list_of_appartments))
        except Exception as ex:
            raise(str(ex))

def replace_appartment_menu(splitted_answer_from_user, list_of_appartments):
    if len(splitted_answer_from_user) == REPLACE_CONDITION and splitted_answer_from_user[INDEX_ABOVE_TO_REMOVE_EXPENSES] == 'with':
        try:
            appartment_number = int(splitted_answer_from_user[VALUE_APPARTMENT])
            amount_to_increase_facilities = int(splitted_answer_from_user[VALUE_TO_REPLACE_UTILITIES])
            utilities = {'water', 'gas', 'electricity', 'heating', 'other'}
            if splitted_answer_from_user[VALUE_UTILITIES_TO_CHANGE] in utilities:
                list_of_appartments[appartment_number]['utilities'][splitted_answer_from_user[VALUE_UTILITIES_TO_CHANGE]] = amount_to_increase_facilities
                history_of_modification_lists.append(copy.deepcopy(list_of_appartments))
        except Exception as ex:
            raise(str(ex))


""" D - FILTER """
"""
filter gas – keep only expenses for gas
filter 300 – keep only expenses having an amount of money smaller than 300 RON
"""
def  fiter_expenses_according_to_amount(list_of_appartments, amount_money_to_be_smaller_for_expenses):
    for index, appartment in enumerate(list_of_appartments):
        if get_sum_expenses(appartment) > amount_money_to_be_smaller_for_expenses:
            remove_all_utilities_for_appartment(appartment)

def filter_expenses_according_to_utilities(list_of_appartments, expense_type):
    for index, appartment in enumerate(list_of_appartments):
        value_selected_expense_type = int(appartment['utilities'][expense_type])
        remove_all_utilities_for_appartment(appartment)
        appartment['utilities'][expense_type] = value_selected_expense_type

def filter_appartment_menu(splitted_answer_from_user, list_of_appartments):
    global history_of_modification_lists
    utilities = {'water', 'gas', 'electricity', 'heating', 'other'}
    if splitted_answer_from_user[VALUE_APPARTMENT] in utilities:
        filter_expenses_according_to_utilities(list_of_appartments, splitted_answer_from_user[VALUE_APPARTMENT])
        history_of_modification_lists.append(copy.deepcopy(list_of_appartments))
    else:
        try:
            amount_money_to_be_smaller_for_expenses = int(splitted_answer_from_user[VALUE_APPARTMENT])
            fiter_expenses_according_to_amount(list_of_appartments, amount_money_to_be_smaller_for_expenses)
            history_of_modification_lists.append(copy.deepcopy(list_of_appartments))
        except Exception as ex:
            raise(str(ex))


"""
(E) Undo
"""

def undo_operation_menu(list_of_tenants):
    global history_of_modification_lists
    if len(history_of_modification_lists) != 0:
        history_of_modification_lists.pop()
        list_of_tenants = history_of_modification_lists[-1]
        return list_of_tenants

    else:
        raise IndexError