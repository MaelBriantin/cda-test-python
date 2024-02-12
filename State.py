from StateMachine import StateMachine

class State:
    def __init__(self, stateMachine: StateMachine) -> None:
        self.__stateMachine = stateMachine

    def doAction(self):
        ...