class CalculationObserver:
    def update(self, calculation):
        pass  # pragma: no cover


class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def execute(self):
        result = self.operation.execute(self.a, self.b)
        for observer in self.observers:
            observer.update(self)
        return result