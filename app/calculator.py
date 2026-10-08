from app.calculator_memento import CalculatorMemento
from app.history import History
from app.operations import OperationFactory
from app.calculation import Calculation
from app.calculator_config import HISTORY_FILE
import os


class Calculator:
    def __init__(self):
        self.history = History()
        self.undo_stack = []
        self.redo_stack = []
        if os.path.exists(HISTORY_FILE):
            self.history.load(HISTORY_FILE) 

    def save_state(self):
        state = self.history.get_history().copy()
        self.undo_stack.append(CalculatorMemento(state)) 

    def undo(self):
        if self.undo_stack:
            current_state = self.history.get_history().copy()
            self.redo_stack.append(CalculatorMemento(current_state))
            memento = self.undo_stack.pop()
            self.history.calculations = memento.get_state()

    def redo(self):
        if self.redo_stack:
            current_state = self.history.get_history().copy()
            self.undo_stack.append(CalculatorMemento(current_state))
            memento = self.redo_stack.pop()
            self.history.calculations = memento.get_state()

    def calculate(self, operation_name, a, b):
        self.save_state()
        operation = OperationFactory.create(operation_name)
        calculation = Calculation(a, b, operation)
        result = calculation.execute()
        self.history.add(f"{a} {operation_name} {b} = {result}")
        self.history.save(HISTORY_FILE)
        self.redo_stack.clear()
        return result

    