import pandas as pd
from app.history import History

def test_history_starts_empty():
    history = History()
    assert isinstance(history.get_history(), pd.DataFrame)
    assert history.get_history().empty

def test_add_to_history():
    history = History()
    history.add("test calculation")
    assert history.get_history().iloc[0]["calculation"] == "test calculation"

def test_save_history(tmp_path):
    history = History()
    history.add("test calculation")
    filename = tmp_path / "history.csv"
    history.save(filename)
    assert filename.exists()

def test_load_history(tmp_path):
    history = History()
    history.add("test calculation")
    filename = tmp_path / "history.csv"
    history.save(filename)

    loaded_history = History()
    loaded_history.load(filename)

    assert loaded_history.get_history().iloc[0]["calculation"] == "test calculation"

def test_clear_history():
    history = History()
    history.add("test calculation")
    history.clear()
    assert history.get_history().empty