from app.calculation import Calculation
from app.operations import Addition

def test_calculation_addition():
    calculation = Calculation(5, 3, Addition())
    assert calculation.execute() == 8


def test_observer_is_notified():
    calculation = Calculation(5, 3, Addition())

    class TestObserver:
        def __init__(self):
            self.notified = False

        def update(self, calculation):
            self.notified = True

    observer = TestObserver()
    calculation.add_observer(observer)
    calculation.execute()

    assert observer.notified