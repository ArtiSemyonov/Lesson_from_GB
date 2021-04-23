from time import sleep


class TrafficLight:
    TrafficLight_count = 0

    # внутри функции предлагает пайч сделать __init__ это обязательно для данной задачи или лучше?
    def running(self, color_1, color_2, color_3):
        self.color_1 = color_1
        sleep(7)
        self.color_2 = color_2
        sleep(2)
        self.color_3 = color_3
        sleep(5)
        TrafficLight.TrafficLight_count += 1


a = TrafficLight()
a.running("RED", "YELLOW", "GREEN")
print(a.color_1)
print(a.color_2)
print(a.color_3)
