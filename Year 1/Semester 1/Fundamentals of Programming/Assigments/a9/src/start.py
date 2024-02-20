from src.ui.ui import UI
from src.repository.MemoryRepository import MemoryRepository
from src.repository.TextFileRepository import TextFileRepository
from src.repository.BinaryFileRepository import BinaryFileRepository
from jproperties import Properties

def delete_file_contents(file_name):
    try:
        with open(file_name, 'w') as file:
            # This truncates the file, effectively deleting its contents
            pass  # You can optionally write something here if needed
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def get_repo_from_properties_file():
    configs_properties = Properties()

    with open('settings.properties', 'rb') as config_file:
        configs_properties.load(config_file)

    repository_string = configs_properties.get("REPO").data
    repository_name = ""

    if repository_string == "Memory":
        repository_name = MemoryRepository()
    elif repository_string == "Text":
        repository_name = TextFileRepository
    elif repository_string == "Binary":
        repository_name = BinaryFileRepository

    else:
        raise ValueError(f"Invalid repository type specified in settings.properties: {repository_string}")

    return repository_name



delete_file_contents("students.txt")
delete_file_contents("grades.txt")
delete_file_contents("disciplines.txt")

delete_file_contents("students.bin")
delete_file_contents("grades.bin")
delete_file_contents("disciplines.bin")

UI = UI(get_repo_from_properties_file())
UI.print_ui()
