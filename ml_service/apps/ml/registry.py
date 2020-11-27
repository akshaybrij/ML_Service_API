from apps.endpoints.models import Endpoint,MLAlgorithm,MLAlgorithmStatus,MLRequest

class MLRegistry:
    def __init__(self):
        self.endpoint = {}

    def add_algorithm(self,endpoint_name,algorithm_object,algorithm_name,algorithm_status,algorithm_version,owner,description,algorithm_code):
        endpoint,_ = Endpoint.objects.get_or_create(name=endpoint_name,owner=owner)
        database_object,algorithm_created = MLAlgorithm.objects.get_or_create(
                name = algorithm_name,
                description=description,
                code=algorithm_code,
                version=algorithm_version,
                owner = owner,
                parent_endpoint=endpoint)
        if algorithm_created:
            status = MLAlgorithmStatus(status=algorithm_status,active=True,created_by=owner,parent_mlalgorithm=database_object)
            status.save()
        self.endpoint[database_object.id]=algorithm_object


        
