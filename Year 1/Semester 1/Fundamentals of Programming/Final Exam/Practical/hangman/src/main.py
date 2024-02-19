from src.controller.controller import Controller
from src.repository.text_file_repository import TextFileRepository
from src.ui.ui import Ui

if __name__ == "__main__":
    repository = TextFileRepository()
    controller = Controller(repository)
    ui = Ui(controller)
    ui.run_app()
