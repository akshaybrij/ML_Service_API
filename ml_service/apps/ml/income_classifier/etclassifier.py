import joblib
import pandas as pd
import os

class ExtraTreeClassifier:
    def __init__(self):
        self.artifact = "apps/ml/income_classifier/research/"
        self.model_path = os.path.join(self.artifact,'et.joblib')
        self.missing_val_path = os.path.join(self.artifact,'na_val.joblib')
        self.encoder_path = os.path.join(self.artifact,'encoder.joblib')

    def preprocessing(self,input_data):
        input_data = pd.DataFrame(input_data,index=[0])
        self.missing_val = joblib.load(self.missing_val_path)
        input_data.fillna(self.missing_val)
        self.encoder = joblib.load(self.encoder_path)
        for key in self.encoder.keys():
            cat_convert = self.encoder[key]
            input_data[key] = cat_convert.fit_transform(self.encoder[key])
        return input_data

    def predict(self,input_data):
        self.model = joblib.load(self.model_path)
        prediction = self.model.predict_proba(input_data)
        return prediction

    def postprocessing(self,prediction):
        label = "<=50K"
        if label > 0.5:
            label = ">=50K"
        return {"label":label,"prediction":prediction,"status":"OK"}

    def compute_prediction(self,input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)
            return self.postprocessing(prediction)
        except Exception as e:
            print(str(e))


