from time import sleep
class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def traffic_light(self):

        for num, el in enumerate(TrafficLight.__color):
            print(f'{TrafficLight.__color[num]}')
            if num == 0:
                sleep(7)
            else:
                sleep(2)

test = TrafficLight()
test.traffic_light()