from State import State

class StateMachine():
    def __init__(self, state: State) -> None:
        self.__actualState = state

    def setState(self, state: State) -> None:        
        self.__actualState = state

    def doAction(self) -> None :
        self.__actualState.doAction()