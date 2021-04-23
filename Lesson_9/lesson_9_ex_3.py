class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    income_dict = {"wage": 10, "bonus": 5}
    pos = Position('Sylvester', 'Stallone', income_dict, "MMM MMM")
    print(pos.get_total_income())
    print(pos.get_full_name())
