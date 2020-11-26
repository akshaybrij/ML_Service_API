from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from apps.endpoints.models import Endpoint,MLAlgorithm,MLAlgorithmStatus,MLRequest
from apps.endpoints.serializers import MLAlgorithmSerializer, EndpointSerializer,MLAlgorithmStatusSerializer,MLRequestSerializer

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

