class Agent:
    def __init__(self, player_id: int = 0) -> None:
        self.player_id = 0
    def fire(self):
        #print('pew pew pew')
        ...
    def patrol(self):
        #print('huh!? What was that?')
        ...


class SpecialAgent(Agent):
    def __init__(self, player_id: int = 0) -> None:
        super().__init__(player_id)

    def fire(self):
        print('pew pew pew')
        ...

    def patrol(self):
        print('huh!? What was that?')
        print('That must be the wind')
        ...