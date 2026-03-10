from django.shortcuts import render
from .models import Carousel

def home(request):
    carousel = Carousel.objects.first()

    return render(request, 'home/home.html', {
        'carousel': carousel
    })