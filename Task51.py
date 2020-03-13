from time import sleep


class TrafficLight:
    __colore = ("red", "yelow", "green")

    def running(self):
        while True:
            for i, colore in enumerate(self.__colore):
                print(f"now is {i} {colore}")
                sleep(7) if colore == "red" or colore == "green" else sleep(2)


ob = TrafficLight()
ob.running()
