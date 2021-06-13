class Road:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def massa(self, ms=25, sm=5):
        a = (self.length * self.width * ms * sm) / 1000
        return f"{a} т."


lng = int(input("Длина:  "))
wid = int(input("Ширина:  "))
my_road = Road(lng, wid)
print(my_road.massa())
