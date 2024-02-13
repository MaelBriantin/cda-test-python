import state.interfaces as interfaces

class StateMachine():
    def __init__(self, state: interfaces.IState) -> None:
        self.__actualState = state

    def setState(self, state: interfaces.IState) -> None:        
        self.__actualState = state

    def doAction(self) -> None :
        self.__actualState.doAction()