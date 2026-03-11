from django.shortcuts import render
from .models import Carousel, Fact, Service, Project, Testimonial

def home(request):
    carousels = Carousel.objects.all()
    facts = Fact.objects.all().order_by("order")
    services = Service.objects.all().order_by("order")
    projects = Project.objects.all().order_by("order")
    testimonials = Testimonial.objects.all().order_by("order")





    return render(request, 'home/home.html', {
        'carousels': carousels,
        'facts': facts,
        'services': services,
        'projects': projects,
        'testimonials': testimonials




    })