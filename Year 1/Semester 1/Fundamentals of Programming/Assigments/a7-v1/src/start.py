from ui.ui import UI
from src.repository.MemoryRepository import MemoryRepository
from src.repository.TextFileRepository import TextFileRepository
from src.repository.BinaryFileRepository import BinaryFileRepository
from src.repository.JSONRepository import JSONRepository
from src.repository.DataBaseRepository import DataBaseRepository

from jproperties import Properties

def get_repo_from_properties_file():
    configs_properties = Properties()

    with open('settings.properties', 'rb') as config_file:
        configs_properties.load(config_file)

    repository_string = configs_properties.get("REPO").data
    repository_name = ""

    if repository_string == "Memory":
        repository_name = MemoryRepository()
    elif repository_string == "Text":
        repository_name = TextFileRepository()
    elif repository_string == "Binary":
        repository_name = BinaryFileRepository()
    elif repository_string == "JSON":
        repository_name = JSONRepository()
    elif repository_string == "DB":
        repository_name = DataBaseRepository()
    else:
        raise ValueError(f"Invalid repository type specified in settings.properties: {repository_string}")

    return repository_name



ui = UI(get_repo_from_properties_file())
ui.print_ui()