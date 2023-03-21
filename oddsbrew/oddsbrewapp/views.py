from django.shortcuts import render
from django.http import HttpResponse
from .findPicks import main
# Create your views here.

def display_data(request):
    data = main()
    return render(request, 'oddsbrewapp/data.html', {'data': data})
