from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.


def aboutPage(request):
    return render(request, 'about_us.html')
    