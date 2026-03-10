from django.contrib import admin
from .models import Carousel, CarouselImage


class CarouselImageInline(admin.TabularInline):
    model = CarouselImage
    extra = 3


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselImageInline]