from django.shortcuts import render
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)
        compound_score = sentiment_scores['compound']
        if compound_score >= 0.05:
            sentiment = 'Positive'
        elif compound_score <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        return render(request, 'sentiment_analysis/result.html', {'sentiment': sentiment})
    return render(request, 'sentiment_analysis/index.html')
