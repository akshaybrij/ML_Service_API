from django.test import TestCase
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from rest_framework.test import APIClient
from .registry import MLRegistry
import inspect

class MLTests(TestCase):
    def setUp(self):
        self.input_data = {
            "age": 37,
            "workclass": "Private",
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States"
                }

    def test_rf_algorithm(self):
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(self.input_data)
        self.assertEqual('OK',response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K',response['label'])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoint),0)
        endpoint_name = "income_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name="Random Forest"
        algorithm_status="Production"
        algorithm_version="1.0"
        owner="admin"
        description="Adding Random Forest Income Classifier"
        algorithm_code= inspect.getsource(RandomForestClassifier)
        registry.add_algorithm(endpoint_name,algorithm_object,algorithm_name,algorithm_status,algorithm_version,owner,description,algorithm_code)
        self.assertEqual(len(registry.endpoint),1)

    '''def test_predict_view(self):
        client = APIClient()
        classifier_url='/api/v1/income_classifier/predict'
        response = client.post(classifier_url,self.input_data,format='json')
        self.assertEqual(response.data['label'],"<=50K")
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)
'''

        
