import j2l.pytactx.agent as pytactx
from getpass import getpass
import time
import event
import state.state as state
import state.state_machine as state_machine

import os
from dotenv import load_dotenv

load_dotenv()   

class AttackState(state.State):    
    def __init__(self, parentFSM: state_machine.StateMachine, agent: pytactx.Agent) -> None:
        super().__init__(parentFSM)
        self.__agent = agent
        self.__xEnemy = 0
        self.__yEnemy = 0
    def __str__(self) -> str:
       return "AttackState"
    def doAction(self):
        if self.__agent.x == self.__xEnemy and self.__agent.y == self.__yEnemy:
            self._stateMachine.setState(ScanState(self._stateMachine, self.__agent))
            return
        self.__agent.fire(True)
        self.__agent.setColor(0,255,0)
        self.__agent.move(0,0)
        if len(self.__agent.range) != 0:
            for enemyName, enemyAttributes in self.__agent.range.items():
                self.__xEnemy, self.__yEnemy = enemyAttributes["x"], enemyAttributes["y"]
                break
        
class ScanState(state.State):
    cp = [(2,2), (2,18), (18,18), (18,2)]
    icp = 0
    def __init__(self, parentFSM: state_machine.StateMachine, agent: pytactx.Agent) -> None:
        super().__init__(parentFSM)
        self.__agent = agent
    def __str__(self) -> str:
       return "ScanState"
    def doAction(self):
        if self.__agent.distance != 0:
            self._stateMachine.setState(AttackState(self._stateMachine, self.__agent))
            return
        self.__agent.fire(False)
        self.__agent.setColor(0,255,255)
        cpx, cpy = ScanState.cp[ScanState.icp]
        if self.__agent.x == cpx and self.__agent.y == cpy:
            ScanState.icp = (ScanState.icp + 1) % len(ScanState.cp)
        self.__agent.moveTowards(cpx, cpy)
        
class SpecialAgent:
    def __init__(self) -> None:
        self.__agent = pytactx.Agent(playerId=os.getenv("ROBOT_ID"),
                      arena=os.getenv("ARENA"),
                      username="demo",
                      password=os.getenv("PASSWORD"),
                      server="mqtt.jusdeliens.com",
                      verbosity=2)
        self.__fsm = state_machine.StateMachine(None)
        self.__fsm.setState(ScanState(self.__fsm, self.__agent))
    def update(self):
        self.__agent.update()
        self.__fsm.doAction()

agent = SpecialAgent()

while True:
   agent.update()

  