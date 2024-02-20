
class Command:
    def __init__(self, fun_name, *fun_params):
        self.__fun_name = fun_name
        self.__fun_params = fun_params

    def call(self):
        return self.__fun_name(*self.__fun_params)

    def __call__(self, *args, **kwargs):
        return self.call()


class Operation:
    def __init__(self, undo_command: Command, redo_command: Command):
        self.__undo = undo_command
        self.__redo = redo_command

    def undo(self):
        return self.__undo()

    def redo(self):
        return self.__redo()


class CascadianOperation:
    def __init__(self, functions : list):
        self.functions = functions

    def undo(self):
        for command in self.functions:
            command.undo()

    def redo(self):
        for command in self.functions:
            command.redo()
