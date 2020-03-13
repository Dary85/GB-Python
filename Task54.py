import random
class Car:
    def __init__(self, **param):
        self.speed = param["speed"]
        self.color = param["colore"]
        self.name = param["name"]
        self.is_police = param["is_police"]

    def getinfo(self):
        infpolice = 'not police' if not self.is_police else 'is police car'
        print(f"This car info:{({'name':self.name, 'colore':self.color,'police':infpolice})}")

    def go(self):
        print(f"Car {self.name} is moving now")

    def stop(self):
        print(f"Car {self.name} stoped")

    def turn(self, direction="forward"):
        print(f"Car {self.name} move {direction}")

    def show_speed(self):
        print(f"Car {self.name} current speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Car {self.name} current speed is {self.speed}")
        try:
            if int(self.speed) > 60:
                print("Worning, excessive speed! acceptable speed 60 km per hour")
        except ValueError:
            print("Smth wrong")


class SportCar(Car):
    def getinfo(self):
        super().getinfo()


class WorkCar(Car):
    def show_speed(self):
        print(f"Car {self.name} current speed is {self.speed}")
        try:
            if int(self.speed) > 40:
                print("Worning, excessive speed! acceptable speed 40 km per hour")
        except ValueError:
            print("Smth wrong")


class PoliceCar(Car):
    def getinfo(self):
        super().getinfo()

def caraction(car):

    directions = ("forward", "turn right", "turn left", "reverse")
    i = random.randint(0,3)
    car.getinfo()
    car.go()
    car.show_speed()
    car.turn(directions[i])
    car.stop()
i=0
while i<5:
    t1 = TownCar(name="Town car"+str(i), speed=random.randint(10,100), is_police=False, colore="black")
    caraction(t1)
    t2 = PoliceCar(name="Police car"+str(i), speed=random.randint(10,100), is_police=True, colore="green")
    caraction(t2)
    t3 = SportCar(name="Sport car"+str(i), speed=random.randint(90,250), is_police=False, colore="yelow")
    caraction(t3)
    t4 = WorkCar(name="Work car"+str(i), speed=random.randint(10, 100), is_police=False, colore="red")
    caraction(t4)
    i+=1