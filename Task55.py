class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки.")
class Pen(Stationery):
    def draw(self):
        print(f"Start draw.{self.title}")
class Pencil(Stationery):
    def draw(self):
        print(f"начали рисовать.{self.title}")
class Handle(Stationery):
    def draw(self):
        print(f"Не рисует ничего.{self.title}")

a1 = Pen("Pen")
a1.draw()
a2 = Pencil("Pencil")
a2.draw()
a3 = Handle("Handle")
a3.draw()
a4= Stationery("Stationery")
a4.draw()
