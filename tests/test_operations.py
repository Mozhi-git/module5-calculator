import pytest
from app.operations import Addition, Subtraction, Multiplication, Division, Power, Root, OperationFactory

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (5, 5, 10),
])
def test_addition(a, b, expected):
    result = Addition().execute(a, b)
    assert result == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (10, 4, 6),
])
def test_subtraction(a, b, expected):
    result = Subtraction().execute(a, b)
    assert result == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (4, 5, 20),
])
def test_multiplication(a, b, expected):
    result = Multiplication().execute(a, b)
    assert result == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (12, 3, 4),
])
def test_division(a, b, expected):
    result = Division().execute(a, b)
    assert result == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 8),
    (5, 2, 25),
])
def test_power(a, b, expected):
    result = Power().execute(a, b)
    assert result == expected

@pytest.mark.parametrize("a,b,expected", [
    (9, 2, 3),
    (8, 3, 2),
])
def test_root(a, b, expected):
    result = Root().execute(a, b)
    assert result == expected

@pytest.mark.parametrize("operation_name,expected_class", [
    ("add", Addition),
    ("subtract", Subtraction),
    ("multiply", Multiplication),
    ("divide", Division),
    ("power", Power),
    ("root", Root),
])
def test_operation_factory(operation_name, expected_class):
    operation = OperationFactory.create(operation_name)
    assert isinstance(operation, expected_class)

def test_division_by_zero():
    with pytest.raises(ValueError):
        Division().execute(10, 0)

def test_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.create("banana")