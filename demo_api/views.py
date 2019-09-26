from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

TOKEN = 'you-token-here'  # Enter your api key here

def index(request):
    return render(request, 'index.html')

def details(request):
    search = request.POST.get('search')
    if search != '':
        url = f'https://trefle.io/api/plants?token={TOKEN}&q={search.lower()}'
        r = requests.get(url)
        data = json.loads(r.text)
        title = f"Search Request of '{search}' is successful"
        parmas = {'title' : title, 'data' : data}
        return render(request, 'details.html', parmas)
    else:
        return HttpResponse('Sorry ! You have not searched anything')
