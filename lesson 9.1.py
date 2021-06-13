import time


class TrafficLight:
    def __init__(self):
        self.color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        while True:
            print(self.color[0])
            time.sleep(7)
            print(self.color[1])
            time.sleep(2)
            print(self.color[2])
            time.sleep(15)


a = TrafficLight()
a.running()
