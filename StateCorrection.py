class IState:
    def doAction(self):
        pass

    def __str__(self) -> str:
        return 'IState'
    
class StateMachine:
    def __init__(self, initialState: IState) -> None:
        self.__state= initialState

    def doAction(self) -> None :
        if self.__state is not None:
            self.__state.doAction()

    def getState(self, newState: IState) -> None:        
        self.__state = newState

class State(IState):
    def __init__(self, parentFSM: StateMachine) -> None:
        self.__parent = parentFSM

    def doAction(self):
        pass

    def __str__(self) -> str:
        return 'State'