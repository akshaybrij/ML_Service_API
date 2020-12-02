from django import forms
from django.forms import ModelForm

from .models import Sentiment,Movie

class SentimentModelForm(ModelForm):
    class Meta:
        model = Sentiment
        help_text = {
            'reviews':"Enter a short review"
                }
        fields = [
                "reviews",
                "gender",
                "age",
                "country"
                ]

    def __init__(self,*args,**kwargs):
        super(SentimentModelForm,self).__init__(*args,**kwargs)
        self.fields['movie'] = forms.ModelChoiceField(queryset=Movie.objects.all())
        self.fields['movie'].required = True


