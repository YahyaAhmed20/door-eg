from django.shortcuts import render
from .models import Catalog

def catalog(request):
    catalogs = Catalog.objects.all()
    return render(request, 'catalog/catalog.html', {'catalogs': catalogs})