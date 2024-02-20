from src.domain.commandthatcanbecalled import *
from src.domain.UndoRedoError import UndoRedoError
class UndoService:
    def __init__(self):
        self.__undo_operation_stack = []
        self.__redo_operation_stack = []

    def register_operation(self, operation: OperationThatCascades):
        self.__undo_operation_stack.append(operation)

    def undo(self):
        if not self.__undo_operation_stack:
            raise UndoRedoError("No more undos!")

        undo_operation = self.__undo_operation_stack.pop()
        self.__redo_operation_stack.append(undo_operation)
        undo_operation.undo()

    def redo(self):
        if not self.__redo_operation_stack:
            raise UndoRedoError("No more redos!")

        redo_operation = self.__redo_operation_stack.pop()
        self.__undo_operation_stack.append(redo_operation)
        redo_operation.redo()