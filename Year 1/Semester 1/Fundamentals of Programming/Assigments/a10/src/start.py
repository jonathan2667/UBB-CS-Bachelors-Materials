from ui.ui import UI
from tests.tests import TestBoard


tests = TestBoard()
tests.testAll()


ui = UI()

ui.run()