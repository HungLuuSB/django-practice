from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
    'december': 'Work on a RTS game until completion'
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_capitalized = month.capitalize()
        month_url = reverse('month-challenge', args=[month])
        list_items += f"<li><a href=\"{month_url}\">{month_capitalized}</a></li>"

    response_form = f"""
    <ul>
        {list_items}
    </ul>
    """
    return HttpResponse(response_form)

def monthly_challenge(request, month:str):
    if month in monthly_challenges:
        return HttpResponse(monthly_challenges[month])
    else:
        return HttpResponse('Invalid month')
