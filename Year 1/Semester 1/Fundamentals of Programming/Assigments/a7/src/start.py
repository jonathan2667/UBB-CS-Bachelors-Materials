from ui.ui import UI
from src.repository.MemoryRepository import MemoryRepository
from src.repository.TextFileRepository import TextFileRepository
from src.repository.BinaryFileRepository import BinaryFileRepository
from src.repository.JSONRepository import JSONRepository
from src.repository.DataBaseRepository import DataBaseRepository
from tests.tests import Test
from jproperties import Properties

def test_all_reporsitories():
  memo_repo_test = MemoryRepository()
  text_repo_test = TextFileRepository("students_test.txt")
  bin_repo_test = BinaryFileRepository("students_test.bin")

  tests_memory_repository = Test(memo_repo_test)
  # tests_memory_repository.test_all()

  tests_memory_repository = Test(text_repo_test)
  # tests_memory_repository.test_all()

  tests_memory_repository = Test(bin_repo_test)
  # tests_memory_repository.test_all()

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


test_all_reporsitories()

ui = UI(get_repo_from_properties_file())
ui.print_ui()