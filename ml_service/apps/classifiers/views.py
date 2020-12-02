from django.shortcuts import render
import joblib
import os
from .forms import SentimentModelForm
from .models import Movie,Sentiment
from .vectorize import vect

classifier = joblib.load('classifier.joblib')

def classify(reviews):
    text = vect.transform(review)
    import pdb;pdb.set_trace()
    classifier.predict(text)
    
def train(review,y):
    x = vect.transform([review])
    text = classifier.partial_fit(x,[y])
    
def classify_review(request):
    form = SentimentModelForm(request.POST or None)
    if form.is_valid():
        reviews = form.cleaned_data.get("reviews")
        gender = forms.cleaned_data.get("gender")
        age = forms.cleaned_data.get("age")
        country = forms.cleaned_data.get("country")
        movie = forms.cleaned_data.get("movie")
        result,proba = classify(reviews)

        context = {
            "result":result,
            "probablity": round(proba * 100,2),
            "review": review,
            "gender": gender,
            "age": age,
            "country": country,
            "movie": movie
                }
        return render(request,"classifiers/prediction.html",context)
    return render(request,"classifier/movie_review.html",context={"form":form})

def feedback(request):
    feedback = request.POST['feedback_button']
    pass






