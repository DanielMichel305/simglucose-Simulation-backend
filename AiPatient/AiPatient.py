import tensorflow as tf 
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
import pandas as pd



#Body weight is not provided in initial dataset so we're gonna estimate an avg weighted male at 75kg


targetGlucose = 115.0

maxDosage = 10.0
maxPerHour = 12.0

DIA = 200 #Duration insulin Action (el w2t eli el insulin byb2a f3al feh) 200 d2ee2a 3.3 hours 


class AiPatient():
    def __init__(self):
        self._bodyWeight = 75
        self._TDD = 0.5 / self._bodyWeight #total daily insulin dose
        self._ICR = 500 / self._TDD  #insulin2Carb ratio
        self._ISF = 1800 / self._TDD #insulin sensitivity
        self._totalDeliveredInsulin = 0
        self._lastReadingsBuffer = pd.DataFrame()

        try:
            self._predictionModel = load_model('./AiPatient/PatientData/glucose_lstm_model.h5', custom_objects={'mse': MeanSquaredError()})
        except:
            Exception("Failed to Load Glucose Prediction Model!")

    def _updateTDD(self):
        alfa = 0.8
        self._TDD = alfa*self._TDD+(1-alfa)*self._totalDeliveredInsulin

    def suggestDose(self, currentGlucose, carbIntake, modelPredictedGlucose=None):
        mealBolus = carbIntake / self._ICR if carbIntake > 0 else 0
        rawCorrection = (currentGlucose-targetGlucose) / self._ISF

        if modelPredictedGlucose is not None:
            predectidedCorrectionBolus = (modelPredictedGlucose-targetGlucose) / self._ISF
            actualCorrection = max(rawCorrection, predectidedCorrectionBolus)
        else:
            actualCorrection = rawCorrection        #this doesn't include any mealBolus data!!!! This also doesn't factor current insulin on board!!! (IMPORTANT WAWA)
        
        finalBolus = min(maxDosage, actualCorrection)
        return finalBolus
    
    def _predictGlucsoeNextStep(self):
        





    

