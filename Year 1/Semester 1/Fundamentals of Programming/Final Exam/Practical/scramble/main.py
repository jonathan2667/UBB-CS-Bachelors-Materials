from src.controller.controller import Controller
from src.repository.repository import Repository
from src.ui.ui import Ui

if __name__ == "__main__":
    repository = Repository()
    controller = Controller(repository)
    ui = Ui(controller)
    print("     WELCOME TO SCRAMBLE!")
    print()
    ui.gameplay()
