from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse

# Create your views here.
def about(request):
    # return HttpResponse('about page')
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse('contact page')
    return render(request, 'contact.html')

def gallery(request):
    # return HttpResponse('gallery page')
    return render(request, 'gallery.html')

def reviews(request):
    # return HttpResponse('reviews page')
    return render(request, 'reviews.html')

