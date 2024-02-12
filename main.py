class Agent:
    def __init__(self, x: int, y: int) -> None:
        """
        Create a new agent with the given x and y coordinates.
        """
        self.__x = 0
        self.__y = 0
    def beforeUpdate(self):
        # print('beforeUpdate')
        ...
    def afterUpdate(self):
        # print('afterUpdate')
        ...
    def update(self):
        self.beforeUpdate()
        print('updated')
        self.afterUpdate()


class DroneAgent(Agent):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x,y)

    def afterUpdate(self):
        print('Agent method override')


class RobotAgent(Agent):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)

    def afterUpdate(self) -> None:
        print('RobotAgent afterUpdate')
        ...
    
class Battlefield:
    def __init__(self, agents:list[Agent]) -> None:
        self.__agents:list[Agent] = agents
    def update(self):
        for agent in self.__agents:
            agent.update()

myBattlefield = Battlefield([DroneAgent(0, 0), RobotAgent(10, 10)])
myBattlefield.update()
