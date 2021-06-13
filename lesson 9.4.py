class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина({self.name}) поехала"

    def stop(self):
        return f"Машина({self.name}) остановилась"

    def turn(self, direction):
        return f"Машина({self.name}) повернула {direction}"

    def show_speed(self):
        return f"Скорость машины({self.name}): {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Скорость машины({self.name}): {self.speed}. Превышение скорости!"
        else:
            return f"Скорость машины({self.name}): {self.speed}"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Скорость машины({self.name}): {self.speed}. Превышение скорости!"
        else:
            return f"Скорость машины({self.name}): {self.speed}"


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


work_car = WorkCar("Грузовик", "хаки", 40)
work_car.go()
work_car.turn("направо")
print(work_car.show_speed())
work_car.turn("налево")
work_car.stop()

work_car = PoliceCar("Полиция", "белый", 90)
work_car.go()
work_car.turn("направо")
print(work_car.show_speed())
work_car.turn("налево")
work_car.stop()

work_car = SportCar("Спорт", "желтый", 120)
work_car.go()
work_car.turn("направо")
print(work_car.show_speed())
work_car.turn("налево")
work_car.stop()

work_car = TownCar("'town'", "черная", 61)
work_car.go()
work_car.turn("направо")
print(work_car.show_speed())
work_car.turn("налево")
work_car.stop()
