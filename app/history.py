import pandas as pd
class History:
    def __init__(self):
        self.calculations = pd.DataFrame(columns=["calculation"])

    def add(self, calculation):
        self.calculations = pd.concat(
            [self.calculations, pd.DataFrame([{"calculation": calculation}])],
            ignore_index=True
    )

    def get_history(self):
        return self.calculations

    def save(self, filename):
        self.calculations.to_csv(filename, index=False)

    def load(self, filename):
        self.calculations = pd.read_csv(filename)

    def clear(self):
        self.calculations = pd.DataFrame(columns=["calculation"])