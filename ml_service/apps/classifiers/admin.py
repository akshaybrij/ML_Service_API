from django.contrib import admin
from .models import Sentiment,Movie

class SentimentModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Sentiment
    list_display = ['__all__']

admin.site.register([Sentiment,Movie])
