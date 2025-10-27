import pandas as pd
import time
from Patient import Patient

simulationRunning = True

patientType = int(input('Enter Patient Type \n1)child \n2)adolescent \n3)Adult\n'))

patient = Patient(patientType)

simStartime = patient.getSimStartTime()
print('======')

print(simStartime)

print(f"Glucose at sim start time (should be 145 ish) {patient.getGlucoseLevelAtTimestamp(simStartime)}") #Bug: First timestamp is +2hrs from start!
