import state.state_machine as state_machine
import state.interfaces as interfaces

class State(interfaces.IState):
    def __init__(self, stateMachine: state_machine.StateMachine) -> None:
        self._stateMachine = stateMachine

    def doAction(self):
        ...