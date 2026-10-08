from app.calculator import Calculator

def test_save_state():
    calculator = Calculator()
    calculator.save_state()
    assert len(calculator.undo_stack) == 1

def test_undo(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator.HISTORY_FILE", tmp_path / "history.csv")

    calculator = Calculator()
    calculator.save_state()
    calculator.history.add("test calculation")
    calculator.undo()
    assert calculator.history.get_history().empty

def test_redo(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator.HISTORY_FILE", tmp_path / "history.csv")

    calculator = Calculator()
    calculator.save_state()
    calculator.history.add("test calculation")
    calculator.undo()
    calculator.redo()

    assert calculator.history.get_history().iloc[0]["calculation"] == "test calculation"


def test_calculate():
    calculator = Calculator()
    result = calculator.calculate("add", 5, 3)
    assert result == 8

def test_calculate_adds_to_history(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator.HISTORY_FILE", tmp_path / "history.csv")

    calculator = Calculator()
    calculator.calculate("add", 5, 3)

    assert calculator.history.get_history().iloc[0]["calculation"] == "5 add 3 = 8"

def test_calculate_undo(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator.HISTORY_FILE", tmp_path / "history.csv")

    calculator = Calculator()
    calculator.calculate("add", 5, 3)
    calculator.undo()

    assert calculator.history.get_history().empty

def test_calculate_redo(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator.HISTORY_FILE", tmp_path / "history.csv")

    calculator = Calculator()
    calculator.calculate("add", 5, 3)
    calculator.undo()
    calculator.redo()

    assert calculator.history.get_history().iloc[0]["calculation"] == "5 add 3 = 8"

def test_calculate_auto_save(tmp_path, monkeypatch):
    monkeypatch.setattr("app.calculator.HISTORY_FILE", tmp_path / "history.csv")

    calculator = Calculator()
    calculator.calculate("add", 5, 3)

    assert (tmp_path / "history.csv").exists()