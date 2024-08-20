from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return HttpResponse('rohit is best opener in world')
def hardik(request):
    return render(request,'hardik.html')
