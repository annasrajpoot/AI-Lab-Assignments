# Lab 2: Smart Room Mode Control


class RoomAgent:

    def __init__(self):
        self.mode = "OFF"

    def control(self, temperature, people):

        if people > 0 and temperature > 25:
            target = "COOLING"
        elif people > 0:
            target = "NORMAL"
        else:
            target = "OFF"

        if target == self.mode:
            command = "No command"
        else:
            command = "Change to " + target
            self.mode = target

        print("Previous mode:", self.mode)
        print("Temperature:", temperature)
        print("People:", people)
        print("Target:", target)
        print("Command:", command)
        print()


agent = RoomAgent()

agent.control(28, 2)
agent.control(28, 2)
agent.control(22, 1)
agent.control(22, 0)
