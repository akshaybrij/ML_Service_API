from django.db import models

class Endpoint(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

class MLAlgorithm(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    code = models.CharField(max_length=10000)
    version = models.CharField(max_length=10)
    owner = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    parent_endpoint = models.ForeignKey(Endpoint,on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):
    status = models.CharField(max_length=127)
    active = models.BooleanField()
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm,on_delete = models.CASCADE)

class MLRequest(models.Model):
    input_data = models.CharField(max_length = 10000)
    full_response = models.TextField()
    response = models.TextField()
    feedback = models.CharField(max_length=1000,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm,on_delete=models.CASCADE)


