from src.ui.ui import UI

UI = UI()
while True:
    try:
        UI.print_ui()
    except Exception as ex:
        print(ex)
