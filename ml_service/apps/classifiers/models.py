from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Sentiment(models.Model):
    Gender_Choice = (
            ('Male','Male'),
            ('Female','Female')
            )
    Country_Choice = (
            ('USA','USA'),
            ('Canada','Canada'),
            ('Mexico','Mexico'),
            ('Europe','Europe')
            )
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    reviews = models.TextField()
    results = models.IntegerField()
    gender = models.CharField(max_length = 10,choices=Gender_Choice)
    age = models.IntegerField()
    country = models.CharField(max_length=30,choices=Country_Choice)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

