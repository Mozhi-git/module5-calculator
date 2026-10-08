from app.calculator_repl import run_repl

def test_repl_exit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    run_repl()

def test_repl_help(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Commands:" in captured.out

def test_repl_history(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr("app.calculator.HISTORY_FILE", tmp_path / "history.csv")

    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Empty DataFrame" in captured.out

def test_repl_clear(monkeypatch):
    inputs = iter(["clear", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

def test_repl_undo(monkeypatch):
    inputs = iter(["undo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

def test_repl_redo(monkeypatch):
    inputs = iter(["redo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

def test_repl_save(monkeypatch):
    inputs = iter(["save", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

def test_repl_load(monkeypatch):
    inputs = iter(["load", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

def test_repl_calculation(monkeypatch, capsys):
    inputs = iter(["add 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "8.0" in captured.out

def test_repl_division_by_zero(monkeypatch, capsys):
    inputs = iter(["divide 10 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero" in captured.out

def test_repl_invalid_number(monkeypatch, capsys):
    inputs = iter(["add hello 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Error: Invalid number" in captured.out

def test_repl_invalid_operation(monkeypatch, capsys):
    inputs = iter(["banana 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Error: Invalid operation" in captured.out

def test_repl_unknown_command(monkeypatch):
    inputs = iter(["hello", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_repl()