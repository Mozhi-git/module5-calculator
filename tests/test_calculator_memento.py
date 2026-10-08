from app.calculator_memento import CalculatorMemento

def test_memento_stores_state():
    memento = CalculatorMemento("test state")
    assert memento.get_state() == "test state"