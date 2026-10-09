# Lab 3: Model Based Reflex Agent


class RoomAgent:

    def __init__(self):
        self.fan = False
        self.heater = False

    def check_room(self, temperature):

        if temperature > 28 and self.fan == False:
            self.fan = True
            print(temperature, "C: Fan ON")

        elif temperature <= 28 and self.fan == True:
            self.fan = False
            print(temperature, "C: Fan OFF")

        else:
            print(temperature, "C: No fan change")


        if temperature < 18 and self.heater == False:
            self.heater = True
            print(temperature, "C: Heater ON")

        elif temperature >= 18 and self.heater == True:
            self.heater = False
            print(temperature, "C: Heater OFF")

        else:
            print(temperature, "C: No heater change")



temperatures = [16, 20, 30, 30, 17]

agent = RoomAgent()

for temp in temperatures:
    agent.check_room(temp)
