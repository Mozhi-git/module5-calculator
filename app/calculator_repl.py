from app.calculator import Calculator
from app.calculator_config import HISTORY_FILE
from app.input_validators import validate_number
from app.exceptions import InvalidNumberError

def run_repl():
    calculator = Calculator()

    while True:
        command = input("Enter command: ")
        parts = command.split()

        if command == "exit":
            break

        elif command == "help":
            print("Commands: help, history, clear, undo, redo, save, load, exit")

        elif command == "history":
            print(calculator.history.get_history())

        elif command == "clear":
            calculator.history.clear()

        elif command == "undo":
            calculator.undo()

        elif command == "redo":
            calculator.redo()

        elif command == "save":
            calculator.history.save(HISTORY_FILE)

        elif command == "load":
            calculator.history.load(HISTORY_FILE)

        elif len(parts) == 3:
            try:
                operation_name = parts[0]
                a = validate_number(parts[1])
                b = validate_number(parts[2])
                result = calculator.calculate(operation_name, a, b)
                print(result)
            except (ValueError, InvalidNumberError) as error:
                print(f"Error: {error}")

if __name__ == "__main__":
    run_repl()

            