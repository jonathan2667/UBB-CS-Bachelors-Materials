#
# Functions section
#

def create_cofee(name, country_of_origin, price):
    """
    We create an object coffee that has 3 properties given by the parameters:

    :param name: Parameter gets the name of the coffee. e.g "Caffe Miel"
    :param country_of_origin: Parameter gets the country of origin of the coffe e.g. "France"
    :param price: Parameter gets the price of the coffe, e.g "5.5"
    :return: We return an object so - called "coffee" in a dictionary format that has the properties from above
    """

    return {
        'name': name,
        'country_of_origin': country_of_origin,
        'price': price
    }

def get_name(coffee):
    """
    Using this function, we get the name of the object Coffee.

    :param coffee: Parameter gets a coffee object.
    :return: It returns the name of the coffee.
    """
    return coffee['name']

def get_country_of_origin(coffee):
    """
    Using this function, we get the name of the country of origin of the oject Coffee.

    :param coffee: Parameter gets a coffee object.
    :return: It returns the country of origin of the coffee.
    """
    return coffee['country_of_origin']

def get_price(coffee):
    """
    Using this function, we get the price of the oject Coffee.

    :param coffee: Parameter gets a coffee object.
    :return: It returns the price of the coffee.
    """
    return coffee['price']

def add_coffee(coffee_list, coffee):
    """
    Using this function, we add in the coffees list a new coffee using the append method.

    :param coffee_list: Parameter gets the list of all coffes where we stored our objects coffee
    :param coffee: Parameter gets a new object coffee
    :return:
    """
    coffee_list.append(coffee)

def validate_cofee(cofee):
    """
    Using this function we validate the price of the coffee(MUST BE GREATER THAN 0), otherwise we raise an error with the name : "Price less than 0"

    :param cofee: Parameter gets a new object coffee
    :return:
    """
    errors = ""
    if get_price(cofee) <= 0:
        errors += "Price less than 0. Not added!"
    if (len(errors)) > 0:
        raise Exception(errors)

def manage_add_coffe(coffee_list, name, country_of_origin, price):
    """
    Using this function, we create a new object coffee with the properies: name, country_of_origin, price and we validate it raising an exception in case
    it does not correspond to the property of a 'correct' coffee (price less than 0) and we add the coffee to the coffee list.

    :param coffee_list: Parameter gets the coffe lists used to store all the coffees object
    :param name: Parameter gets the name of the coffee. e.g "Caffe Miel"
    :param country_of_origin: Parameter gets the country of origin of the coffe e.g. "France"
    :param price: Parameter gets the price of the coffe, e.g "5.5"
    :return:
    """
    cofee = create_cofee(name, country_of_origin, price)
    validate_cofee(cofee)
    add_coffee(coffee_list, cofee)


def sorting_alphabetically_by_country_and_price(coffee_list):
    sorted_list = sorted(coffee_list, key = lambda x:x['country_of_origin'])

    for i in range (len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if get_country_of_origin(sorted_list[i]) == get_country_of_origin(sorted_list[j]):
                if get_price(sorted_list[i]) > get_price(sorted_list[j]):
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    return sorted_list

def filter_by_country_price(coffee_list, country_of_origin, price):
    filtered_coffes = []
    for coffee in coffee_list:
        if get_country_of_origin(coffee) == country_of_origin and get_price(coffee) <= price:
            filtered_coffes.append(coffee)

    return filtered_coffes

#
# User interface section
#


def ui_add_coffee(coffee_list):
    name = input("Name ")
    country_of_origin = input("country_of_origin ")
    price = float(input("Price "))

    manage_add_coffe(coffee_list, name, country_of_origin, price)

def ui_display_cofee_sorted(coffee_list):
    sorted_coffee_list = sorting_alphabetically_by_country_and_price(coffee_list)
    for coffe in sorted_coffee_list:
        print(coffe)

def ui_print_commands(commands):
    print("Menu!!!\n")
    for c in commands:
        print(c)

def ui_print_smaller_price(coffee_list, price):
    printed = False
    for coffee in coffee_list:
        if get_price(coffee) <= price:
            print(coffee)
            printed = True
    if (printed == False):
        print("No such coffees")

def ui_print_from_country(coffee_list, country_of_origin):
    printed = False
    for coffe in coffee_list:
        if get_country_of_origin(coffe) == country_of_origin:
            print(coffe)
            printed = True
    if (printed == False):
        print("No such coffees")

def ui_filter_by_country_price(coffee_list):
    country_of_origin = input("country_of_origin ")
    price = input("Price ")

    if country_of_origin == "":
        price = float(price)
        ui_print_smaller_price(coffee_list, price)
    elif price == "":
        ui_print_from_country(coffee_list, country_of_origin)
    else:
        price = float(price)
        filtered_coffes = filter_by_country_price(coffee_list, country_of_origin, price)
        for filtered_coffee in filtered_coffes:
            print(filtered_coffee)

def ui_run():
    coffee_list = [
        {'name': 'Caffe Miel', 'country_of_origin': 'France', 'price': 5.5} ,
        {'name': 'Caffe Noir', 'country_of_origin': 'Allemagne', 'price': 13.5} ,
        {'name': 'Caffe Blanc','country_of_origin': 'Allemagne', 'price': 6.5} ,
        {'name': 'Caffe Bleu', 'country_of_origin': 'Angleterre', 'price': 6.7} ,
        { 'name': 'Caffe Rouge', 'country_of_origin': 'Gabon', 'price': 12.7}
    ]

    commands = {'ui_add_coffee':ui_add_coffee, 'ui_display_cofee_sorted':ui_display_cofee_sorted, 'ui_filter_by_country_price':ui_filter_by_country_price}
    ui_print_commands(commands)
    while True:
        cmd = input(">>>")
        cmd = cmd.strip()
        if (cmd == ""):
            continue
        elif cmd == "exit":
            return
        else:
            if cmd in commands:
                try:
                    commands[cmd](coffee_list)
                except Exception as ex:
                    print(str(ex))
            else:
                print("Not in the commands!!")


def main():
    ui_run()

main()

