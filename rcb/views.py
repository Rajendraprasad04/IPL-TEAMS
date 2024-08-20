from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat (request):
    return HttpResponse('<center>virat is king of cricket</center>')
def abd(request):
    return render(request,'abd.html')
    