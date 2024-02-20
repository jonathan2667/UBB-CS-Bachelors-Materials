
class CommandThatCanBeCalled:
    def __init__(self, fun_name, *fun_params):
        self.__fun_name = fun_name
        self.__fun_params = fun_params

    def call(self):
        return self.__fun_name(*self.__fun_params)

    def __call__(self, *args, **kwargs):
        return self.call()


class Operation:
    def __init__(self, undo_command: CommandThatCanBeCalled, redo_command: CommandThatCanBeCalled):
        self.__undo = undo_command
        self.__redo = redo_command

    def undo(self):
        return self.__undo()

    def redo(self):
        return self.__redo()


class OperationThatCascades:
    def __init__(self, functions: list):
        self.undo_redo_functions = functions

    def add_operation(self, operation):
        self.undo_redo_functions.append(operation)

    def undo(self):
        for applied_function in self.undo_redo_functions:
            applied_function.undo()

    def redo(self):
        for applied_function in self.undo_redo_functions:
            applied_function.redo()