from django.shortcuts import render
from django.http import HttpResponse
import re
from collections import Counter


def index(request):
    return render(request, 'analyzer/index.html')


def analyze(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        word_count = len(re.findall(r'\b\w+\b', text))
        sentence_count = len(re.findall(r'[.!?]', text))
        words = re.findall(r'\b\w+\b', text.lower())
        most_common_words = Counter(words).most_common(5)

        context = {
            'text': text,
            'sentence_count': sentence_count,
            'most_common_words': most_common_words
        }
        return render(request, 'analyzer/results.html', context)
    return HttpResponse('Error: No text provided.')



