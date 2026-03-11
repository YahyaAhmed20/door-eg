from django.contrib import admin
from .models import Carousel, CarouselImage,Fact,Service,Project,Testimonial


class CarouselImageInline(admin.TabularInline):
    model = CarouselImage
    extra = 3


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselImageInline]

admin.site.register(Fact)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order")


admin.site.register(Service, ServiceAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "order")

admin.site.register(Project, ProjectAdmin)



class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "profession", "order")

admin.site.register(Testimonial, TestimonialAdmin)