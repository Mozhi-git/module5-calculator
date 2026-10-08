class Operation:
    def execute(self, a, b):
        pass  # pragma: no cover

class Addition(Operation):
    def execute(self, a, b):
        return a + b

class Subtraction(Operation):
    def execute(self, a, b):
        return a - b

class Multiplication(Operation):
    def execute(self, a, b):
        return a * b


class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Power(Operation):
    def execute(self, a, b):
        return a ** b

class Root(Operation):
    def execute(self, a, b):
        return a ** (1 / b)

class OperationFactory:
        @staticmethod
        def create(operation_name):
            if operation_name == "add":
               return Addition()
            elif operation_name == "subtract":
                return Subtraction()
            elif operation_name == "multiply":
                return Multiplication()
            elif operation_name == "divide":
                return Division()
            elif operation_name == "power":
                return Power()
            elif operation_name == "root":
                return Root()
            else:
                raise ValueError("Invalid operation")