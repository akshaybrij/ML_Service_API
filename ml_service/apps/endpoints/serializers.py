from rest_framework import serializers
from .models import Endpoint,MLAlgorithm,MLAlgorithmStatus,MLRequest

class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        fields = ('id','name','owner','created_on')

class MLAlgorithmSerializer(serializer.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self,mlalgorithm):
        return self.MLALgorithmStatus.objects.filter(parent_mlalgorithm=mlalgorithm)

    class Meta:
        model = MLAlgorithm
        read_only_fields = ('id','name','description','code','version','owner','created_at','parent_endpoint')
        fields = read_only_fields

class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithmStatus
        read_only_fields = ('id','active')
        fields = '__all__'

class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = (
                'id',
                'input_data',
                'full_response',
                'response',
                'feedback',
                'created_at',
                'parent_mlalgorithm'
                )
        fields = '__all__'



