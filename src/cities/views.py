from django.shortcuts import render
from django.http import HttpResponse

CODES = {
    "AAL": "Aalborg, Denmark",
    "ANX": "Andenes, Norway",
    "ARN": "Stockholm, Sweden",
    "AEY": "Akyreyri, Iceland",
}

def cities(request, code):
    citycountry = CODES.get(code.upper(), "Undefined")
    ctx = {
        'code': code.upper(),
        'citycountry': citycountry,
        }
    return render(request, template_name='citypage.html', context=ctx)

def home(request):
    return render(request, template_name='home.html', context={})