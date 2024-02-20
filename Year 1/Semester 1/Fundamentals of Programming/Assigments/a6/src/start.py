#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#

import ui

def main():
    ui.print_menu()
    list_of_appartments = []
    ui.get_input_user(list_of_appartments)

main()