from django.shortcuts import render
from oddsbrewapp.findPicks import main
from django.core.cache import cache
# Create your views here.

def display_data(request):
    data, alldata = main()
    print(data)
    print(alldata)
    return render(request, 'oddsbrewapp/data.html', {'data': data, 'alldata': alldata})
