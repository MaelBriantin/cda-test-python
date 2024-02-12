from State import State
from StateMachine import StateMachine
from Agent import Agent

class ScanState(State):
    def __init__(self, stateMachine: StateMachine, agent: Agent) -> None:
        super().__init__(stateMachine)
        self.__agent = agent

    def doAction(self):
        self.__agent.patrol()


class AttackState(State):
    def __init__(self, stateMachine: StateMachine, agent: Agent) -> None:
        super().__init__(stateMachine)
        self.__agent = agent

    def doAction(self):
        self.__agent.fire()