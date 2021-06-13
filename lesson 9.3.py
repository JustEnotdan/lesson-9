class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self.income.values())}"


a = Position("Имя", "Фамилия", "работник", 12345678, 500)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
