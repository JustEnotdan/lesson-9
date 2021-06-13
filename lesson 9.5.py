class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f"{self.title}: Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"𝔻𝕣𝕒𝕨𝕚𝕟𝕘 {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"𝓦𝓻𝓲𝓽𝓲𝓷𝓰 {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"🅟🅐🅘🅝🅣🅘🅝🅖 {self.title}")

t = input("Введите текст(желательно на английском): ")

a1 = Pen(t)
a1.draw()

a2 = Pencil(t)
a2.draw()

a3 = Handle(t)
a3.draw()