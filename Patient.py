import pandas as pd
from datetime import datetime
PATIENT_FILES_PATH = './patientData' 
patientTypeFile = {
    1 : 'child',
    2 : 'adolescent',
    3 : 'adult'
}
class Patient:
    def __init__(self, patientType=3):
        if patientType < 1 or patientType > 3:
            ValueError(f'{patientType} is Not a valid patient type!')
            return
        
        
        self._paientSimulationDataFrame = pd.read_csv(f'{PATIENT_FILES_PATH}/{patientTypeFile[patientType]}.csv')
        self._paientSimulationDataFrame['Time'] = pd.to_datetime(self._paientSimulationDataFrame['Time'])

        
        self._patientType = patientTypeFile[patientType]
        print(self._paientSimulationDataFrame.columns)


    def getSimStartTime(self):
        date = pd.to_datetime(self._paientSimulationDataFrame.head(1)['Time'],).iloc[0]
        date = date.tz_localize('UTC')
        return int(date.timestamp())
        

    def _getRowAtNearestTimestamp(self, timestamp):
        
        
        targetTimeStamp = datetime.fromtimestamp(timestamp)
        timestamp = pd.to_datetime(timestamp)
        
        idx = (self._paientSimulationDataFrame['Time'] - targetTimeStamp).abs().idxmin()

        return self._paientSimulationDataFrame.iloc[idx]
    
    def getGlucoseLevelAtTimestamp(self, timestamp):
    
        glucoseLevel = self._getRowAtNearestTimestamp(timestamp=timestamp)['BG']
        return glucoseLevel