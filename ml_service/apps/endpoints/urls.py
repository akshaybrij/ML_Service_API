from django.urls import path,include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndPointViewSet,MLAlgorithmViewSet,MLAlgorithmStatusViewSet,MLRequestViewSet,PredictView


router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints",EndPointViewSet,basename='endpoints')
router.register(r"algorithms",MLAlgorithmViewSet,basename='mlalgorithm')
router.register(r"status",MLAlgorithmStatusViewSet,basename='mlalgorithmstatus')
router.register(r"requests",MLRequestViewSet,basename='mlrequests')

urlpatterns = [
        path('api/v1/',include(router.urls)),
        path('api/v1/<endpoint_name>/predict/',PredictView.as_view(),name='predict')
        ]
