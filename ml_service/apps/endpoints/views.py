import json
import joblib
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import views,status
from rest_framework.response import Response
from apps.endpoints.models import Endpoint,MLAlgorithm,MLAlgorithmStatus,MLRequest
from apps.endpoints.serializers import MLAlgorithmSerializer, EndpointSerializer,MLAlgorithmStatusSerializer,MLRequestSerializer
from apps.ml.registry import MLRegistry

class EndPointViewSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()

class MLAlgorithmViewSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()

def deactivate_other_statuses(instance):
    old_status = MLAlgorithStatus.objects.filter(parant_mlalgorithm=instance.parent_mlalgorithm,create_at__lt=instance.created_at,active=True)
    for i in old_status:
        old_status[i].active = False
    MLAlgorithStatus.objects.bulk_update(old_status,['active'])

class MLAlgorithmStatusViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = MLAlgorithmStatusSerializer
    queryset = MLAlgorithmStatus.objects.all()

    def perform_create(self,serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                deactivate_other_statuses(instance)
        except Exception as e:
            raise APIException(str(e))

class MLRequestViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,viewsets.GenericViewSet,mixins.UpdateModelMixin):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()

class PredictView(views.APIView):
    def post(self,request,endpoint_name,format=None):
        algorithm_status = request.query_params.get("status","production")
        algorithm_version = request.query_params.get("version")
        algs = MLAlgorithmStatus.objects.filter(parent_mlalgorithm__parent_endpoint__name=endpoint_name,status=algorithm_status,active=True)
        if algorithm_version is not None:
            algs = algs.filter(version=algorithm_version)

        if len(algs) == 0:
            raise Exception("No version defined")

        alg_index=0
        registry = joblib.load('registry.joblib')
        algorithm_object = registry[algs[alg_index].id]
        prediction =algorithm_object.compute_prediction(request.data)
        if prediction["label"]:
            label = prediction["label"]
        else:
            raise Exception("Bad Request")
        ml_req = MLRequest(
                input_data = json.dumps(request.data),
                full_response = prediction,
                response= label,
                feedback="",
                parent_mlalgorithm =algs[alg_index].parent_mlalgorithm)
        ml_req.save()
        prediction['request_id']= ml_req.id
        return Response(prediction,status=status.HTTP_200_OK)

