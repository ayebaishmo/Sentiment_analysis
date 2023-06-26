from django.urls import path
from sentiment_analysis.views import analyze_sentiment

urlpatterns = [
    path('', analyze_sentiment, name='analyze_sentiment'),
]

