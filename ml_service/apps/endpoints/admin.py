from django.contrib import admin
from .models import Endpoint,MLAlgorithm,MLAlgorithmStatus,MLRequest

admin.site.register([Endpoint,MLAlgorithm,MLAlgorithmStatus,MLRequest])
