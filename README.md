# Module 5 - Enhanced Calculator

This is a Python command-line calculator that supports arithmetic operations, calculation history, undo and redo, and saving and loading history using pandas.

The application uses design patterns including Factory, Strategy, Observer, Memento, and Facade.

## Installation

1. Clone the GitHub repository.
2. Open the project folder.
3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

5. Install the required libraries:

```bash
python -m pip install pytest pytest-cov pandas python-dotenv
```

## Usage

Start the calculator:

```bash
python -m app.calculator_repl
```

Example calculation:

```text
Enter command: add 5 3
8.0
```

Available operations:
- add
- subtract
- multiply
- divide
- power
- root

Available commands:
- help
- history
- clear
- undo
- redo
- save
- load
- exit

## Testing

Run all tests:

```bash
python -m pytest
```

Run tests with statement and branch coverage:

```bash
python -m pytest --cov=app --cov-branch --cov-report=term-missing tests/
```

## Configuration

The calculator uses a `.env` file for configuration.

Create a `.env` file in the main project folder with:

```text
HISTORY_FILE=history.csv
```

The calculator automatically saves calculation history to this CSV file and loads existing history when it starts.