"""
WSGI config for ml_service project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ml_service.settings')

application = get_wsgi_application()

import json
import joblib
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.etclassifier import ExtraTreeClassifier

try:
    registry = MLRegistry()
    rf = RandomForestClassifier()
    registry.add_algorithm(endpoint_name='income_classifier',
                           algorithm_object=rf,
                           algorithm_name='random forest',
                           algorithm_status='production',
                           algorithm_version='1.0.0',
                           owner='admin',
                           description='Random Forest Income Classifier',
                           algorithm_code=inspect.getsource(RandomForestClassifier)
                           )
    et = ExtraTreeClassifier()
    registry.add_algorithm(endpoint_name='income_classifier',
                           algorithm_object= et,
                           algorithm_name='extratreeclassifier',
                           algorithm_status='production',
                           algorithm_version='1.0.0',
                           owner='admin',
                           description='Extra Tree Classifier',
                           algorithm_code=inspect.getsource(ExtraTreeClassifier))

                           
    joblib.dump(registry.endpoint,'registry.joblib')
except Exception as e:
    print(str(e))


