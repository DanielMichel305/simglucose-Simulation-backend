import time
from datetime import datetime, timedelta

class SimulationClock:
    def __init__(self, startTimestamp: int):
        self._simulationStartTime = startTimestamp
        self._currentSimulationTime = startTimestamp
        self._isRunning = False
    
    def updateClock(self):
        self._isRunning = True
        realStartTime = time.time()
        
        elapsedTimeRealtime = time.time() - realStartTime
        self._currentSimulationTime = self._currentSimulationTime = datetime.fromtimestamp(
            self._simulationStartTime + elapsedTimeRealtime
        )

        
    def getSimulationTime(self):
        return self._currentSimulationTime