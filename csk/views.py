from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dhoni(request):
    return HttpResponse('<h1>Dhoni is one of the best wicket keeper and batsman</h1>')

def raina(request):
    return render(request,'raina.html')
