from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.base import render_value_in_context
from django.urls import reverse
from django.template.loader import render_to_string
monthly_challenges = {
    'january': 'Eat healthy for a month',
    'february': 'Work out at least 3 times a day',
    'march': 'Learn new skills',
    'april': 'Eat an appy a day everyday',
    'may': 'Spend more time outside',
    'june': 'Help with a charity',
    'july': 'Open an evening class',
    'august': 'Only use half of the amount of money spent last month',
    'september': 'Running 2 miles each morning',
    'october': 'Eat vegetables for breakfast',
    'november': 'Learn django for at least 4 hours a day',
    'december': None
}

def index(request):

    return render(request, "challenges/index.html", {
        'months': list(monthly_challenges.keys())
    })

def monthly_challenge(request, month:str):
    if month in monthly_challenges:
        return render(request, "challenges/challenge.html", {
            'month': month.capitalize(),
            'challenge_text': monthly_challenges[month]
        })
    else:
        return HttpResponseNotFound('Invalid month')
