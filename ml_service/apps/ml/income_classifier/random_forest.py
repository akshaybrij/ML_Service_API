import joblib
import pandas as pd

class RandomForestClassifier:
    def __init__(self):
        path = 'apps/ml/income_classifier/research/'
        self.missing_val = joblib.load(path+'na_val.joblib')
        self.encoders = joblib.load(path+'encoder.joblib')
        self.model = joblib.load(path+'rf.joblib')
    
    def preprocessing(self,input_data):
        input_data = pd.DataFrame(input_data,index=[0])
        input_data.fillna(self.missing_val)
        for e in self.encoders.keys():
            cat_conv = self.encoders[e]
            input_data[e] = cat_conv.fit_transform(input_data[e])
        return input_data

    def predict(self,input_data):
        return self.model.predict_proba(input_data)

    def postprocessing(self,input_data):
        label = "<=50K"
        if input_data[1] > 0.5:
            label = ">=50K"
        return {"probablity":input_data[1],"label":label,"status":"OK"}

    def compute_prediction(self,input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]
            prediction = self.postprocessing(prediction)
            return prediction
        except Exception as e:
            return(str(e))
        
     
